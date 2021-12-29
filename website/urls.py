from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.LandingView.as_view(), name='landing'),
    path('landing/', views.LandingView.as_view(), name='landing'),
    path('login/', auth_views.LoginView.as_view(template_name="home/login.html"),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('available/', views.AvailableView.as_view(), name = 'available'),
    path('create_ad/', views.CreateAdView.as_view(), name = 'create_ad'),
    path('landlords/', views.LandlordsView.as_view(), name = 'landlords'),
    path('tenants/', views.TenantsView.as_view(), name = 'tenants'),
    path('help/FAQ/', views.FAQView.as_view(), name = 'FAQ'),
    path('help/safety/', views.SafetyView.as_view(), name = 'safety'),
]
