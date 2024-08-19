from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace = 'api')),
    path('campaign/{campaign_id}/', include('campaigns.urls')),
]
