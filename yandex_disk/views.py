from django.shortcuts import render
import requests as http_requests
from .forms import DiskLink

my_oauth = "y0__xCUtv6zBBjblgMg8q73yxJz1nS4i89l071n_AhTa5fV9oMdhg"
download_str = "https://cloud-api.yandex.net/v1/disk/public/resources?public_key="
download_str_link = f"https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key="
"https://disk.yandex.ru/d/x84j7QbdAJ3rxw"


def process_link(request):
    form = DiskLink()
    return render(request, "index.html", {"form": form})


def check_link(request):
    form = DiskLink(request.POST)
    if form.is_valid():
        str_to_check = form.cleaned_data["link"]
        response = http_requests.get(download_str + str_to_check, headers={"Authorization": f'Bearer {my_oauth}'})
        output_list = list()
        process_response = response.json()
        for item in process_response.get("_embedded").get("items"):
            if item.get("type") == "file":
                download_link = http_requests.get(f"{download_str_link}{str_to_check}&path={item.get('path')}").json()["href"]
                output_list.append({'name': item["name"], 'link': item.get("sizes")[-1].get("url"), "download_link": download_link})
            else:
                output_list.append({'name': item["name"], 'link': item.get("path"), "download_link": ""})
    else:
        return render(request, "index.html", {"form": form})
    if response.status_code == 200:
        return render(request, "template_with_answer.html", {"answer": output_list, 'form': form})

