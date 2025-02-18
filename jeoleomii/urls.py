# jeoleomii/urls.py
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),  # http://127.0.0.1:8000/jeoleomii/ 로 접속 시 index 뷰 실행
]
