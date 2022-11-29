from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View, generic
from .forms import ImageForm
from core.models import Image

# Create your views here.

def indexview (request):
    if request.user.is_authenticated:
        images = Image.objects.filter(owner=request.user)
        context = {'images': images}
        return render(request, 'core/homepage.html', context)
    else:
        return HttpResponseRedirect(reverse('login'))
def addview (request):
    
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES, initial={'owner': request.user})
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return HttpResponseRedirect(reverse('core:add'))
    else:
        form = ImageForm(initial={'owner': request.user})
    return render(request, 'core/addpage.html', {'form': form})

def deleteview (request, pk):
    Image.objects.get(id=pk).delete()
    return HttpResponseRedirect(reverse('core:home'))

def allview (request):
    images = Image.objects.all()
    context = {'images': images}
    return render(request, 'core/allview.html', context)
