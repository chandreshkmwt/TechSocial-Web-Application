from django.shortcuts import render
from django.urls import reverse_lazy
from . import form
from django.views.generic import CreateView
# Create your views here.




class SignUp(CreateView):
    form_class = form.UserCreateForm
    #taking user to the login page on successful signup
    success_url = reverse_lazy('login')
    template_name = 'accounts/SignUp.html'
