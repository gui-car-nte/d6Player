from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('register/', views.register, name = 'register'),
    path('login/', views.login_view, name = 'login'),
    path('logout/', views.logout_view, name = 'logout'), # type: ignore # ! look into what causes this warning
    path('campaigns/', include('campaigns.urls')),
]
