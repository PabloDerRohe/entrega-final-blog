from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('index.urls')),
    path('pages/', include('pages.urls')),
    path('accounts/', include('accounts.urls')),
    path('messages/', include('direct.urls')),
    path('admin/', admin.site.urls),
]
