from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<str:username>/<str:campaign_name>/', include('campaigns.urls')),
    path('register/', views.register, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'), # type: ignore # ! look into what causes this warning
]
