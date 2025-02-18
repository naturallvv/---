# jeoleomii/views.py
from django.shortcuts import render

def index(request):
    # jeoleomii/index.html 템플릿을 렌더링
    return render(request, 'jeoleomii/index.html')
