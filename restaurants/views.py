from django.shortcuts import render, redirect
from .models import Restaurant
from .forms import RestaurantForm, SignUpForm , SignInForm
from django.contrib.auth import authenticate , login, logout

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user_obj = form.save(commit =False)
            user_obj.set_password(user_obj.password)
            user_obj.save()
            login(request, user_obj)
            return redirect('restaurant-list')
    context = {
        "form":form,
    }
    return render(request, 'signup.html', context)

def signin(request):
    form = SignInForm()
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            my_username= form.cleaned_data['username']
            my_password = form.cleaned_data['password']
            user_obj= authenticate(username= my_username, password=my_password)
            if user_obj is not None :
                login(request,user_obj)
                return redirect('restaurant-list')
    context = {
        "form":form,
    }
    return render(request, 'signin.html', context)
 

def signout(request):
    logout(request)
    return redirect('restaurant-list') 

def restaurant_list(request):
    context = {
        "restaurants":Restaurant.objects.all()
    }
    return render(request, 'list.html', context)


def restaurant_detail(request, restaurant_id):
    context = {
        "restaurant": Restaurant.objects.get(id=restaurant_id)
    }
    return render(request, 'detail.html', context)

def restaurant_create(request):
    form = RestaurantForm()
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def restaurant_update(request, restaurant_id):
    restaurant_obj = Restaurant.objects.get(id=restaurant_id)
    form = RestaurantForm(instance=restaurant_obj)
    if request.method == "POST":
        form = RestaurantForm(request.POST, request.FILES, instance=restaurant_obj)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    context = {
        "restaurant_obj": restaurant_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def restaurant_delete(request, restaurant_id):
    restaurant_obj = Restaurant.objects.get(id=restaurant_id)
    restaurant_obj.delete()
    return redirect('restaurant-list')
