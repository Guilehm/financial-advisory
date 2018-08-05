from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def login_view(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            authenticated_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, authenticated_user)
            messages.add_message(
                request,
                messages.SUCCESS,
                'Olá, {}, seu login foi efetuado com sucesso'.format(request.user)
            )
            return redirect('core:index')
    return render(request, 'core/login.html', {'login_form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('core:index'))


def register_view(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('core:index')
    return render(request, 'core/register.html', {
        'form': form,
    })
