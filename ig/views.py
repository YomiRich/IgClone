from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def photo_of_day(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'welcome.html',{"images":images, "location": location})

def search_by_category(request):
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        print(search_term)
        found_images = Image.search_by_category(search_term)
        print(found_images)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"images":found_images})
    else:
        message=" Item not found."
        return render(request,'search.html',{"message":message})
    
def search_by_location(request, location):
    locations = Location.objects.all()
    images = Image.search_by_location(location)
    print(images)
    title = f'{location} Photos'
    return render(request, 'location.html', {'title': title, 'images': images, 'locations': locations})

def search_results(request):
    if 'image' in request.GET and request.GET["image"]: 
        search_term = request.GET.get("image")
        found_images = Image.search_by_category(search_term)
        message = f"{search_term}"
        return render(request,'search.html',{"message":message,"images":found_images})
    else:
        message=" Item not found."
        return render(request,'search.html',{"message":message})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect("login")
    else:
        form = SignUpForm()
    return render(request, "registration/signup.html", {"form": form})

@login_required(login_url="login/")
def profile(request):
    current_user = request.user
    user_data = User.objects.get(id=current_user.id)
    user_profile = UserProfile.objects.get(id=current_user.id)

    return render(
        request,
        "registration/profile.html",
        {
            "user_data": user_data,
            "user_profile": user_profile
        },
    )

@login_required(login_url="login/")  # only logged in users should access this
def edit_profile(request):
    current_user = request.user
    user = User.objects.get(id=current_user.id)
    
    # prepopulate UserProfileForm with retrieved user values from above.
    user_form = UserForm(instance=user)
    
    # The sorcery begins from here, see explanation below
    ProfileInlineFormset = inlineformset_factory(
        User, UserProfile, fields=("photo", "phone", "bio", "neighbourhood")
    )
    formset = ProfileInlineFormset(instance=user)
    
    if request.user.is_authenticated and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)
            
        if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(
                    request.POST, request.FILES, instance=created_user
                )
        
        if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return redirect("profile")
                
        return render(
            request,
            "registration/edit_profile.html",
            {"noodle": user.id, "noodle_form": user_form, "formset": formset},
        )
    else:
        raise PermissionDenied





    