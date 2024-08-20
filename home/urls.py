from django.urls import path, include
from . import views
from campaigns import views as campaign_views # ! incorrect, circular dependency

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'), # type: ignore # ! look into what causes this warning
    path('<str:username>/<str:campaign_name>/', include('campaigns.urls')),
    path('create-campaign/', campaign_views.create_campaign, name='create_campaign'),
]
