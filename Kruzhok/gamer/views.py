from django.shortcuts import render, redirect
from .models import user
from .forms import userform
from . import sts
from django.utils import timezone

def index(request):
    error = ''
    if request.method == 'POST':
        sss = sts.makeform(request.POST)
        form = userform(sts.makeform(request.POST))
        #print('ddddddddddddddddddddddddddddddd' + type(sts.makeform(sss)))
        ##form = userform(request.POST)
        #ddd = open('run.txt', 'w')
        #ddd.write(str(form))
        #ddd.write('\n \n'+ str(request.POST))
        #ddd.write( '\n \n'+ str(sts.makeform(request.POST)))
        #ddd.close()
        if form.is_valid():
            print(request.POST)
            print(form)
            form.save()
            return redirect('/profile')
        else:
            return redirect('/topsecret')

    form = userform()
    context = {"form": form, "error": error}
    return render(request, 'main/index.html', context)

def profile(request):
    form = user.objects.order_by('-date')[:1]
    return render(request, 'main/profile.html', {'form': form})

def topsecret(request):
    return render(request, 'main/topsecret.html')


