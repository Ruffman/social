from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import auth
from django.urls import reverse_lazy
from django.views.generic import CreateView

from . import forms
from django.views.generic import (TemplateView)

# Create your views here.
class FAQView(TemplateView):
    template_name = 'help/FAQ.html'

class SafetyView(TemplateView):
    template_name = 'help/safety.html'



class LandingView(TemplateView):
    template_name = 'home/landing.html'

class LoginView(TemplateView):
    template_name = 'home/login.html'



class AvailableView(TemplateView):
    template_name = 'objects/available.html'

class CreateAdView(TemplateView):
    template_name = 'objects/create_ad.html'



class LandlordsView(TemplateView):
    template_name = 'people/landlords.html'

class TenantsView(TemplateView):
    template_name = 'people/tenants.html'


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'home/signup.html'
