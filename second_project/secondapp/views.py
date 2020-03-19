from django.shortcuts import render
from secondapp.models import Userinfo
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from secondapp.forms import newuser,UserForm,UserProfileInfoForm
# Create your views here.
def index(request):
    mydict={"insert":"another webpage will lead you to users info."}
    return render(request,"second_app/index.html",mydict)

def users(request):
    user_list=Userinfo.objects.order_by('firstname')
    user_dict={'USERS':user_list}
    return render(request,"second_app/user.html",user_dict)

def form(request):
    Form=newuser()

    if request.method=='POST':
        Form=newuser(request.POST)
        if Form.is_valid():
            Form.save(commit=True)
            return index(request)
        else:
            print("Form is not valid")

    return render(request,"second_app/form.html",{'form':Form})

def other(request):
    return render(request,"second_app/other.html")

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'second_app/registration.html',{'user_form':user_form,
    'profile_form':profile_form,'registered':registered})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed")
            print("username: {} and password: {}".format(username,password))
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'second_app/login.html',{})

@login_required
def special(request):
    return HttpResponse("You are logged in,Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
