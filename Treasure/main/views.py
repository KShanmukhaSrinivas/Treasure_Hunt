from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login as auth_login,  authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from .models import Progress
# Create your views here.

def home(request):
    if request.user.is_authenticated:
        a= Progress.objects.get(user=request.user)
        context={"progress":a}
        return render(request,"main_page.html", context)
    else:
        return redirect("login")
def puzzle1(request, ans):
    a= Progress.objects.get(user=request.user)
    if(ans==1):
        a.level1=True
        a.save()
        print("Changed Value to True")
        return redirect("/")
    print(a.level1)
    return render(request,"level1.html")

def puzzle2(request,ans):
    a= Progress.objects.get(user=request.user)
    if(ans==1):
        a.level2=True
        a.save()
        print("Changed Value to True")
        return redirect("/")
    print(a.level2)
    return render(request,'level2.html')

def puzzle3(request,ans):
    a= Progress.objects.get(user=request.user)
    if(ans==1):
        a.level3=True
        a.save()
        print("Changed Value to True")
        return redirect("/")
    print(a.level3)
    return render(request,'level3.html')

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("/")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="facebook_login.html", context={"login_form":form})

def sigunup(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            messages.success(request, "Registration successful." )
            a= Progress(level1=False, level2= False, level3= False, user=user)
            a.save()
            return redirect("/")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="facebook_register.html", context={"register_form":form})

def logout_view(request):
    logout(request)
    return redirect("login")