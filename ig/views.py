from django.shortcuts import render

# Create your views here.

def profile_of_day(request):
    profile = Profile.objects.all()
    images=Image.objects.all()
    return render(request,'homepage.html',{"images":images, "profile":profile})