from django.shortcuts import render
from .models import Images , Gallery , Politics
from django.contrib import messages
from django.db.models import Q
def frontpage(request):
    # if request.method == 'POST':
    #     query = request.POST.get('query')
    #     places_for = Images.objects.filter(
    #         Q(name__icontains=query) | Q(state__icontains=query)
    #     )
    #     return render(request , 'search_items.html' , {'place':places_for})
    image = Images.objects.all()
    context = {
        'places':image,
    }
    return render(request , 'homepage.html' , context)
    
def gallery(request):
    returned  = Gallery.objects.all()
    context = {
        'pictures':returned,
    }
    return render(request , 'gallery.html',  context)
def add(request):
    if request.method == 'POST':
        # images = Images(name = request.POST.get['name'] , image = request.FILES['image'] , description = request.POST.get['desc'])
        images = Images()
        images.name = request.POST.get('name')
        images.image = request.FILES['image']
        images.description = request.POST.get('desc')
        images.location = request.POST.get('location')
        images.type = request.POST.get('type')
        images.save()
        if images.save():
            messages.success(request ,'Data added')
    context = {
            'messages':messages
        }       
    return render(request , 'renamed.html' , context)   
def add_gallery(request):
    if request.method == 'POST':
        gallery = Gallery()
        gallery.image = request.FILES['image']
        gallery.name = request.POST.get('name')
        gallery.save()
        if gallery.save():
            messages.success(request , 'Picture added')
    context = {
            'messages':messages
        }        
    return render(request , 'add_gallery.html' , context)    
def destinations(request):
    places = Images.objects.all()
    context = {
        'places':places,
    }
    return render(request , 'destinations.html' , context)
def navbar(request):
    return render(request , 'main_navbar.html')    
def politics(request):
    people = Politics.objects.all()
    context = {
        'people':people,
    }    
    return render(request , 'politics.html' , context)
def add_politics(request):
    if request.method == 'POST':
        r = request.POST
        people = Politics(name = r.get('name') , about_khadpu = r.get('about') , facebook = r.get('facebook') , position = r.get('position') , image = request.FILES['image'] )
   
        people.save()
    return render(request , 'add_politics.html')    
# Create your views here.
