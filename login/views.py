from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import CreateUserForm

from django.contrib.auth.decorators import login_required


def home(request):
    return render (request, "login/mainpage.html")

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'user succesfully created')
            return redirect('loginPage')
            
    context = {'form':form}
    return render (request, "login/signUp.html", context)

def loginPage(request):
    if request.method == "POST":
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username = username, password = password)

       if user is not None:
            login(request, user)
            return redirect('logOut')

       else:
        messages.info(request, 'Please enter the correct Username or password')

    return render (request, "login/loginPage.html")

def polls(request):
    return render (request, "login/polls.html")

def chatroom(request):
    return render (request, "login/chatroom.html")

def logOut(request):

    return render (request, "login/logout.html")

    logout(request)
    return redirect('loginPage')

def room(request, room_name):
	return render(request, 'chatroom.html', {
		'room_name': room_name
	})
    



    