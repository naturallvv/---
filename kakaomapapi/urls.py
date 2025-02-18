from django.urls import path
from .views import result_page

urlpatterns = [
    path('', result_page, name='result_page'),
]
