# uploadphoto/views.py
from django.shortcuts import render, redirect
from .forms import UserPhotoForm
#from .ai_utils import find_most_similar_image  # AI 관련 함수가 있다면 사용

def uploadphoto_page(request):
    ai_result = None
    if request.method == 'POST':
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            user_photo = form.save()  # UserPhoto 객체 저장
            # 이후 user_photo.image.path를 통해 AI 유사도 검사 가능
            # 예시:
            # image_folder = os.path.join(settings.MEDIA_ROOT, 'reference_photos')
            # ai_result = find_most_similar_image(user_photo.image.path, image_folder)
            return redirect('uploadphoto_page')
    else:
        form = UserPhotoForm()
    return render(request, 'uploadphoto/uploadphoto.html', {'form': form, 'ai_result': ai_result})
