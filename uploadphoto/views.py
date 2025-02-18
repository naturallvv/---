# uploadphoto/views.py
from django.shortcuts import render, redirect
from .forms import UserPhotoForm

def uploadphoto_page(request):
    if request.method == 'POST':
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # 데이터를 DB에 저장
            # 지금은 아무 추가 데이터 없이 결과 페이지로 단순 리다이렉트
            return redirect('kakaomapapi:result_page')
        else:
            print("폼 에러:", form.errors)
    else:
        form = UserPhotoForm()
    return render(request, 'uploadphoto/uploadphoto.html', {'form': form})
