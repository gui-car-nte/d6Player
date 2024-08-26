from django.urls import path, include
from . import home_views

urlpatterns = [
    path('', home_views.home, name = 'home'),
    path('register/', home_views.register, name = 'register'),
    path('login/', home_views.login_view, name = 'login'),
    path('logout/', home_views.logout_view, name = 'logout'), # type: ignore # ! look into what causes this warning
    path('campaigns/', include('campaigns.campaigns_urls')),
]
