from django.conf.urls import include, re_path
from django.contrib import admin
from  django.conf import  settings
from django.conf.urls.static import static

urlpatterns=[

    re_path("admin/", admin.site.urls),
    re_path("music/", include('music.urls')),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)