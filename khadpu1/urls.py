from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('khadpu' ,views.frontpage , name = 'home' ),
    path('gallery' , views.gallery , name='gallery'),
    path('add_new' , views.add , name = 'add'),
    path('add_gallery' , views.add_gallery , name = 'add_gallery'),
    path('destinations' , views.destinations , name = 'destinations'),
    path('politics' , views.politics , name = 'politics'),
    path('add_politics' , views.add_politics , name = 'add_politics'),
    path('navbar' , views.navbar , name = 'navbar')

]
