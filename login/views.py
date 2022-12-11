from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout

# Create your views here.
from .forms import CreateUserForm, CreatePollForm
from .models import app

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

def createP(request):
    form = CreatePollForm()
    if request.method == "POST":
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls')
    else :
        form = CreatePollForm()
        context = {'form' : form}
        
    return render (request, "polls/create.html", context)

def results(request):
    return render (request, "polls/results.html")

def chatroom(request):
    return render (request, "login/chatroom.html")

def logOut(request):

    return render (request, "login/logout.html")

    logout(request)
    return redirect('loginPage')

    



    