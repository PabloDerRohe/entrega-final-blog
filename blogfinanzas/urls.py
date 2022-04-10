from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('index.urls')),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('messages/', include('direct.urls')),
    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
