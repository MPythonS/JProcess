from django.shortcuts import render, redirect

from users.forms import UserRegisterForm


# Create your views here.

def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('')