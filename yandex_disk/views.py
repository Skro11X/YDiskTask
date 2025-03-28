import requests as http_requests
import json
from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_http_methods
from django.core.cache import cache
from .forms import DiskLink

my_oauth = "y0__xCUtv6zBBjblgMg8q73yxJz1nS4i89l071n_AhTa5fV9oMdhg"
get_yandex_files_link = "https://cloud-api.yandex.net/v1/disk/public/resources?public_key="
download_yandex_link = "https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key="

MIME_CATEGORIES_READABLE = {
    "Без фильтров": "",
    "Текстовые файлы": "text",
    "Изображения": "image",
    "Аудио файлы": "audio",
    "Видео файлы": "video",
    "Документы и архивы": "application",
}


def process_link(request: HttpRequest):
    form = DiskLink()
    return render(request, "base.html", {"form": form})


@require_http_methods(["GET"])
def check_link(request: HttpRequest):
    """
    Обращается к публичной ссылке для доступа к диску
    """
    public_key = request.GET.get("public_key", "")
    path = request.GET.get("path", "")
    type_filter = request.GET.get("filter", "")
    dict_to_return = cache.get_or_set(request.build_absolute_uri(), get_dict_from_link(public_key, path, type_filter), 600)
    if "error" in dict_to_return:
        form = DiskLink()
        return render(request, "template_with_answer.html", {"form": form, "errors": dict_to_return})
    old_path = path[:path.rfind("/")]
    return render(request, "template_with_answer.html",
                  {"answer": dict_to_return,
                   "public_key": public_key,
                   "path": path,
                   "old_path": old_path,
                   "filters": MIME_CATEGORIES_READABLE,
                   "filter": type_filter})


@require_http_methods(["POST"])
def get_link(request: HttpRequest):
    """
    Осуществляет обращение к яндекс диску, чтобы получить у него ссылку для скачивания
    """
    request_body = json.loads(request.body)
    links = request_body.get("selected_files")
    download_files_links = list()
    if isinstance(links, str):
        download_files_links.append(http_requests.get(download_yandex_link + links).json())
    else:
        for link in links:
            download_files_links.append(http_requests.get(download_yandex_link + link).json())
    return JsonResponse(download_files_links, safe=False)


def get_dict_from_link(public_key: str, path: str = "", type_filter: str = ""):
    """
    Делает запрос к яндекс диску с указанием пути, путь нужен, для того чтобы открывать папки
    """
    if path:
        path = "&path=" + path
    response = http_requests.get(get_yandex_files_link + public_key + path + "&limit=100",
                                 headers={"Authorization": f'Bearer {my_oauth}'})
    if response.status_code != 200:
        return {"error": f"Ошибка API: {response.status_code}", "details": response.text}
    output_list = list()
    process_response = response.json()
    for item in process_response.get("_embedded", {}).get("items", {}):
        if item.get("mime_type", False) and not item.get("mime_type").startswith(type_filter):
            continue
        download_link = f"{public_key}&path={item.get('path')}"
        if item.get("sizes", False):
            output_list.append(
                {'name': item['name'],
                 'link': item.get('sizes')[-1].get('url'),
                 'download_link': download_link,
                 'type': item.get('type'),
                 'path': item.get('path')})
        else:
            output_list.append({'name': item["name"],
                                'link': False,
                                'download_link': download_link,
                                "type": item.get("type"),
                                "path": item.get("path")})
    return output_list
