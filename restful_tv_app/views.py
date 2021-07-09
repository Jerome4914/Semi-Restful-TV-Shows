from django.shortcuts import render, redirect
from .models import Show

# Create your views here.

def index(request):
    return redirect("/shows")

def shows(request):
    context={
        'shows': Show.objects.all()
    }
    return render(request, "shows.html", context)

def new(request):
    return render(request, "new_show.html")

def shows_create(request):
    Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'],
    )
    return redirect('/shows')

def edit(request, id):
    one_show = Show.objects.get(id=id)
    context = {
        'show': one_show
    }
    return render(request, 'edit.html', context)

def update(request, id):
    update = Show.objects.get(id=id)
    update.title = request.POST['title']
    update.release_date = request.POST['release_date']
    update.network = request.POST['network']
    update.description = request.POST['description']

    return redirect('/shows')

def show(request, id):
    one_show =Show.objects.get(id=id)
    context = {
        'show': one_show
    }
    return render(request, 'show.html', context)

def delete(request, id):
    delete = Show.objects.get(id=id)
    delete.delete()
    return redirect('/shows')
