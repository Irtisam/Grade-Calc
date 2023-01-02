from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
#<<<<<<< HEAD
#=======

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        username = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

    context = {}
    return render(request, 'calc/login_register.html', context)

def home(request):
    return render(request, 'calc/Home.html')
#>>>>>>> 22df2a2 (modified templates structure)
