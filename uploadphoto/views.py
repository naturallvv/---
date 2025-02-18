from django.shortcuts import render, redirect
from .forms import UserPhotoForm
from .ai_utils import find_most_similar_images  # ai_utils.py의 함수 임포트
from django.conf import settings
import os

def uploadphoto_page(request):
    if request.method == 'POST':
        form = UserPhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save()

            feature_folder = os.path.join(settings.MEDIA_ROOT, 'reference_photos', 'image', 'features')
            location_file = os.path.join(settings.MEDIA_ROOT, 'reference_photos', 'location_info.txt')

            similar_images = find_most_similar_images(photo.image.path, feature_folder, location_file, top_n=3)
            print("AI 결과:", similar_images)

            # .pt → .jpg로 확장자 교체하여 실제 이미지 경로를 구성
            # 예: base_name = "some_image"  →  image_path = "/media/reference_photos/image/some_image.jpg"
            result_list = []
            for pt_filename, loc, sim in similar_images:
                base_name = pt_filename.replace('.pt', '')
                # Django에서 MEDIA_URL = '/media/' 라고 가정
                # => 실제 브라우저에서 /media/reference_photos/image/<base_name>.jpg 로 접근
                image_path = f'/media/reference_photos/image/{base_name}.jpg'

                result_list.append({
                    'name': base_name,       # .pt 확장자 제거
                    'address': loc,         # location_file에서 읽은 지역 정보
                    'similarity': sim,      # 유사도
                    'img': image_path       # 실제 이미지 경로
                })

            request.session['recommended_places'] = result_list
            return redirect('kakaomapapi:result_page')
        else:
            print("폼 에러:", form.errors)
    else:
        form = UserPhotoForm()
    return render(request, 'uploadphoto/uploadphoto.html', {'form': form})
