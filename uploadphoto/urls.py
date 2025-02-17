# uploadphoto/urls.py
from django.urls import path
from .views import uploadphoto_page

urlpatterns = [
    path('', uploadphoto_page, name='uploadphoto_page'),
]
