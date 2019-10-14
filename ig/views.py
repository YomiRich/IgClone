from django.shortcuts import render,redirect
from .models import Location,Image
# Create your views here.
def welcome(request):
    return render(request,'welcome.html')


def photo_of_day(request):
    location = Location.objects.all()
    images=Image.objects.all()
    return render(request,'todayphoto.html',{"images":images, "location": location})

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
        

    