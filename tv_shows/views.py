from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def root(request):
    return redirect('/shows')

def home(request):
    context = {
        'shows': Show.objects.all(),
    }
    return render(request,'tv_shows/shows.html', context)

def new(request):
    context = {
        'network': Network.objects.all()
    }
    return render(request, 'tv_shows/new.html', context)

def create(request):
    if request.method == "GET":
        return redirect('/shows/new')
    elif request.method == "POST":
        title = request.POST["title"]
        network = request.POST['network']

        network_id = request.POST['network']
        network = Network.objects.get(id=network_id)
     
    
        release_date = request.POST['release_date']
        description = request.POST['description']
        obj = Show.objects.create(title=title, description=description, network=network, release_date=release_date)
        obj.save()
        return redirect(f"/shows/{obj.id}")

def info_show(request, show_id):
    context = {
        'show':Show.objects.get(id=show_id)
    }
    return render(request, 'tv_shows/info_show.html', context)

def edit_show(request, show_id):
    context = {
        'show':Show.objects.get(id=show_id),
        'network':Network.objects.all().exclude(show__id=show_id)
    }
    return render(request, 'tv_shows/edit.html', context)

def update(request, show_id):
    if request.method == 'GET':
        return redirect('/shows')
    elif request.method == 'POST':
        show = Show.objects.get(id=show_id)

        new_title = request.POST['title']
        new_description = request.POST['description']
        new_network_id = request.POST['network']

        new_network = Network.objects.get(id=new_network_id)

        new_release_date = request.POST['release_date']

        show.title = new_title
        show.description = new_description
        show.network = new_network
        show.release_date = new_release_date
        show.save()

        return redirect(f"/shows/{show.id}")

def delete(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()

    return redirect('/')

def networks(request):
    context = {
        "network" : Network.objects.all()
    }
    return render(request, "tv_shows/networks.html", context)