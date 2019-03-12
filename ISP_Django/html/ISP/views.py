from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from ISP.forms import *
from database.models import *
from django.core.mail import send_mail, get_connection
from django.shortcuts import render
from django.contrib.auth.hashers import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

#@login_required
def past(request):
    events = Event.objects.all()

    return render(request, 'past.html', {'events': events})

#@login_required
def ongoing(request):
    events = Event.objects.all()
    print(request)
    if request.method == 'POST':
        if request.POST.get("form_type", "") == u'ongoing':
            ongoingform = EventForm(request.POST)
            if ongoingform.is_valid():
                event = ongoingform.save()
        elif request.POST.get("form_type", "") == u'past':
            ongoingform = EventForm()
            Event.objects.filter(id=int(request.POST.get('checks'))).update(completed=True)
            
    else:
        ongoingform = EventForm()

    return render(request, 'ongoing.html', {'ongoingform': ongoingform, 'events': events})

def signin(request):

    if request.method == 'POST':
        if request.POST.get("form_type", "") == u'signup':
            # create a form instance and populate it with data from the request:
            signupform = SignupForm(request.POST)
            loginform = LoginForm()
            # check whether it's valid:
            if signupform.is_valid():
                username = request.POST.get('username', None)
                password = request.POST.get('password', None)

                cd = signupform.cleaned_data
                user = signupform.save(commit=False)
                user.set_password(password)
                user.save()
                
                user = auth.authenticate(username=username, password=password)
                print(bool(user.is_authenticated))
                print('user: ', user)
                if user is not None:
                    auth.login(request, user)
                    return HttpResponseRedirect('/profile')
                con = get_connection('django.core.mail.backends.console.EmailBackend')
                #send_mail(
                    #cd['subject'],
                    #cd['message'],
                    #cd.get('email', 'noreply@example.com'),
                    #['siteowner@example.com'],
                    #connection=con
                #)
        elif request.POST.get("form_type", "") == u'login':
            signupform = SignupForm()
            loginform = LoginForm(request.POST)
            # check whether it's valid:
            if loginform.is_valid():
                username = request.POST['username']
                password = request.POST['password']

                user = auth.authenticate(request, username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return HttpResponseRedirect('/profile')


    else:
        signupform = SignupForm()
        loginform = LoginForm()
    return render(request, 'signup.html', {'signupform': signupform, 'loginform': loginform})