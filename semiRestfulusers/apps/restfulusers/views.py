from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
  # the index function is called when root is visited
from models import *


def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'restfulusers/index.html', context)

def new(request):
    return render(request, 'restfulusers/new.html')

def edit(request, id):
    context = {
        'user': User.objects.get(id=id),
        'id': id
    }
    return render(request, 'restfulusers/edit.html', context)

def show(request, id):
    context = {
        "user": User.objects.get(id=id),
        "id": id
    }
    return render(request, 'restfulusers/user.html', context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/users/new/')
    else:
        User.objects.create(full_name = request.POST['full_name'], email= request.POST['email'])
        a = User.objects.last()
        return redirect('/users/{}'.format(a.id))

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect('/users')

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/users/{}/edit'.format(id))
    a = User.objects.get(id=id)
    a.full_name = request.POST['full_name']
    a.email = request.POST['email']
    a.save()
    return redirect('/users/{}'.format(id))