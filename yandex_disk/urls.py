from django.urls import path
from .views import process_link, check_link, get_link, change_directory


urlpatterns = [
    path('', process_link, name='process_link'),
    path('check_disk/', check_link, name='check_link'),
    path('get_link/<path:link>/', get_link, name='get_link'),
    path('change_directory/', change_directory, name='change_directory'),
]
