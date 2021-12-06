from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('landing/', views.LandingView.as_view(), name = 'landing'),
    path('login/', views.LoginView.as_view(), name = 'login'),
    path('available/', views.AvailableView.as_view(), name = 'available'),
    path('create_ad/', views.CreateAdView.as_view(), name = 'create_ad'),
    path('landlords/', views.LandlordsView.as_view(), name = 'landlords'),
    path('tenants/', views.TenantsView.as_view(), name = 'tenants'),
    path('FAQ/', views.FAQView.as_view(), name = 'FAQ'),
    path('safety/', views.SafetyView.as_view(), name = 'safety'),
]
