from django.shortcuts import render, redirect
from django.contrib import messages
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
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST['description'],                    
        # show.save(),
        # messages.success(request, "Show successfully created")
    )
    return redirect('/shows')

def edit(request, id):
    one_show = Show.objects.get(id=id)
    context = {
        'show': one_show        
    }    
    return render(request, 'edit.html', context)

def update(request, id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{id}/edit')
    else:
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
