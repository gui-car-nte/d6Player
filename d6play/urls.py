from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.home_urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.api_urls', namespace = 'api')),
]
