# Create your views here.

from django.http import HttpResponse

#def index(request):
 #   return HttpResponse("Hello, world. You're at the email_app index.")

from django.shortcuts import render_to_response
from forms import UserForm,LoginForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from models import UserProfile
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import check_password
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required

def error404(request):
    return render_to_response("email_app/404.html")

@login_required
def index(request):
    return render_to_response("email_app/index.html")

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print password
            user=authenticate(username=username,password=password)
            print user
            u=User.objects.get(username=username)
            if user is not None and u.check_password(password):
                if user.is_active:
                    auth_login(request,user)
                else:
                    return render_to_response('email_app/login.html',{'title':'Login', 'form'   :LoginForm()})
            else:
                return render_to_response('email_app/login.html',{'title':'Login', 'form':LoginForm()})
            return HttpResponseRedirect('/')
        else:
            return render_to_response('email_app/login.html',{'title':'Login', 'form':LoginForm()})
    else:
        return render_to_response('email_app/login.html',{'title':'Login', 'form':LoginForm()})
def logout(request):
    user_logout(request)
    return HttpResponseRedirect(reverse("login-user"))

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User(email = form.cleaned_data['email'])
            user.first_name = form.cleaned_data['firstName']
            user.last_name = form.cleaned_data['lastName']
            user.username = user.email
            user.set_password(form.cleaned_data['password'])
            user.is_active = True
            user.save()

            userProfile = UserProfile.objects.get_or_create(user = user,
                           
                            gender = form.cleaned_data['gender'])

            return HttpResponseRedirect(reverse("login-user"))

    else:
        form = UserForm()

    data = {
        'form': form,
        'title': 'SignUp'
    }
    return render_to_response("email_app/signup.html", data)


