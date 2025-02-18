from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('uploadphoto/', include('uploadphoto.urls')),
    path('kakaomapapi/', include(('kakaomapapi.urls', 'kakaomapapi'), namespace='kakaomapapi')),
    path('jeoleomii/', include(('jeoleomii.urls', 'jeoleomii'), namespace='jeoleomii')),
]

# 개발 모드에서 미디어 파일 서빙을 위해
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)