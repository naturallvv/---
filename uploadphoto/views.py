# uploadphoto/views.py
from django.shortcuts import render, redirect
from .forms import PhotoForm

def uploadphoto_page(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()  # 여기서 파일이 저장됨
            # 저장된 photo.image.path를 로그로 찍어 확인해보세요.
            print("저장된 파일 경로:", photo.image.path)
            return redirect('uploadphoto_page')
        else:
            print("폼 에러:", form.errors)
    else:
        form = PhotoForm()
    return render(request, 'uploadphoto/uploadphoto.html', {'form': form})
