from django.urls import path
from .views import process_link, check_link, get_link


urlpatterns = [
    path('', process_link, name='process_link'),
    path('yandex_disk_api/', check_link, name='yandex_disk_api'),
    path('get_link/', get_link, name='get_link'),
]
