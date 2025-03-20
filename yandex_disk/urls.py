from django.urls import path
from .views import process_link, check_link


urlpatterns = [
    path('', process_link, name='process_link'),
    path('check_disk/', check_link, name='check_link'),
]
