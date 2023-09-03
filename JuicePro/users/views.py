from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from users.forms import UserRegisterForm


# Create your views here.
################################# User Registration #################################
def user_registration_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('')
pass    # end of user_registration_view

################################# User Login #################################

def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('order_form')  # Nurodykite URL, į kurį norite nukreipti po sėkmingo prisijungimo
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})
