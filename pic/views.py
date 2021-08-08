from django.shortcuts import render, redirect
from django.contrib import auth
from .models import Picture
import random # This is to generate random objects from the models


def index(request):
    # It is important for all the 'key names' to be the same inorder to work with the buttons "ref:'base.html" on the pages because there are more than one page
    every = Picture.objects.all()
    first_object = random.choice(every) # This will get the initial random object which will then be displayed to the user upon a get request

    if request.user.is_authenticated:

        if request.method == 'POST':
            print(request.POST)

            for one in every: # here, I'm trying to loop over every object or picture in the database inorder to get the current picture that is being displayed on the screen and its ID inorder to work with it through the buttons on the "base.html"
                if request.POST.get('s' + str(one.id)) or request.POST.get('p' + str(one.id)): # these are the smash or pass buttons. Once it passes through here, I have successfully gotten the current picture that is being displayed on the screen which is "one"
                    the_object = random.choice(every)

                    if request.POST.get('s' + str(one.id)): # saving the current picture that is displayed on the screen when the user clicks the "SMASH" button.
                        request.user.sub.create(sub_name=one.name, sub_pictures=one.pictures) # this creates a unique user object

                    return render(request, 'dynamic.html', {'the_object': the_object})

        return render(request, 'base.html', {'the_object': first_object})

    else:
        if request.method == 'POST':
            print(request.POST)
           
            if request.POST.get('smash') or request.POST.get('pass'):
                the_object = random.choice(every)
                return render(request, 'dynamic.html', {'the_object': the_object})

        return render(request, 'base.html', {'the_object': first_object})


def all_smashes(request):
    if request.user.is_authenticated:
        all_pic = request.user.sub.all().order_by('-id') # getting all the available pictures in the requested user
        print(all_pic)
        return render(request, 'all_smashes.html', {'all_pic': all_pic})
    else:
        return render(request, 'notauth.html')


def delete_id(request, id):
    request.user.sub.get(id=id).delete()
    return redirect('/smashes/')


def delete_all(request):
    request.user.sub.all().delete()
    return redirect('/smashes/')

# Create your views here.