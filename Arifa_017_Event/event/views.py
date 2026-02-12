from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import * 
from .forms import *
# Create your views here.

@login_required
def homePage(request):
    return render(request, 'home.html')

def signupPage(request):
    if request.method=="POST":
        full_name=request.POST.get('full_name') 
        username=request.POST.get('username') 
        password=request.POST.get('password') 
        confirm_password=request.POST.get('confirm_password') 
        user_types=request.POST.get('user_types') 
        image=request.FILES.get('image') 

        user_exist=EventUserModel.objects.filter(username=username).exists()
        if user_exist:
            messages.warning(request, 'Username Already Exist')
            return redirect('register')
        if password==confirm_password:
            EventUserModel.objects.create_user(
                full_name=full_name,
                username=username,
                password=password,
                user_types=user_types,
                profile_image=image,
            )
            messages.success(request, "Account created")
            return redirect('login')
        messages.warning(request, "Password Didnot Match")
        return redirect('register')
    return render(request, "auth/register.html")
    
def loginPage(request):
    if request.method=="POST":
        username=request.POST.get('username') 
        password=request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Account Login Succesfully")
            return redirect('home')
        messages.warning(request, "Invalid Credentials")
        return redirect('login')
    return render(request, "auth/login.html")
    
def logoutPage(request):
    logout(request)
    messages.success(request, "Account Logout")
    return redirect('login')

def changepassword(request):
    current_user=request.user
    if request.method=="POST":
        current_password=request.POST.get('current_password')
        new_password=request.POST.get('new_password')
        confirm_password=request.POST.get('confirm_password')

        if check_password(current_password, current_user.password):
            if new_password==confirm_password:
                current_user.set_password(new_password)
                current_user.save()
                update_session_auth_hash(request, current_user)
                messages.success(request, "Password Changed")
                return redirect('home')
    return render(request, "auth/changepassword.html")

def categoryPage(request):
    data=CategoryModel.objects.all()
    return render(request, "category/categorylist.html", {'data':data})

def addcategoryPage(request):
    if request.method=="POST":
        CategoryModel.objects.create(
            name=request.POST.get('name')
        )
        return redirect('category')
    return render (request, "category/addcategory.html")

def editcategoryPage(request, id):
    data=CategoryModel.objects.get(id=id)
    if request.method=="POST":
        data.name=request.POST.get('name')
        data.save()
        return redirect('category')
    return render (request, "category/editcategory.html", {'data':data})

def deletecategoryPage(request, id):
    CategoryModel.objects.get(id=id).delete()
    return redirect('category')

def eventPage(request):
    user=request.user
    if user.user_types == "Admin":
        data=EventModel.objects.all()
    else:
        data=EventModel.objects.filter(created_by=user) 
    return render(request, "event/eventlist.html", {'data':data})

def addeventPage(request):
    event_form=EventForm()
    context={
        'event_form':event_form
    }
    if request.method=="POST":
        event_form=EventForm(request.POST)
        if event_form.is_valid:
            event=event_form.save(commit=False)
            event.created_by=request.user
            event.save()
            return redirect('eventlist')
    return render(request, "event/addevent.html", context)

def editeventPage(request, id):
    data=EventModel.objects.get(id=id)
    event_form=EventForm(instance=data)
    context={
        'event_form':event_form,
        'data':data
    }
    if request.method=="POST":
        event_form=EventForm(request.POST, instance=data)
        if event_form.is_valid:
            event=event_form.save(commit=False)
            event.created_by=request.user
            event.save()
            return redirect('eventlist')
    return render(request, "event/editevent.html", context)

def deleteeventPage(request, id):
    EventModel.objects.get(id=id).delete()
    return redirect('eventlist')

def ViewPage(request, id):
    data=EventModel.objects.get(id=id)
    return render(request, "event/viewevent.html" , {'data':data})

def changestatus(request, id):
    data=EventModel.objects.get(id=id)

    if data.status == "NotStarted":
        data.status = "InProgress"
    elif data.status == "InProgress":
        data.status = "Completed"
    data.save()
    return redirect('eventlist')

