from django.shortcuts import render,redirect    
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from food.models import Item
from .forms import RegisterForm
from django.contrib.auth import logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'welcome {username}!')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})

def custom_logout(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    user = request.user
    user_items = Item.objects.filter(user_name=user)

    context = {
        'user': user,
        'user_items': user_items,
    }

    return render(request, 'users/profile.html', context)

    
