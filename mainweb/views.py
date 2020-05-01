from django.shortcuts import render
from .models import Information
from .models import Gallery
from .models import Testimonianls
from . models import Team

 
 

# Create your views here.
def home(request):
    infom=Information.objects.all()
    testi=Testimonianls.objects.all()
    team=Team.objects.all()
    params={'info':infom,'testi':testi,'tea':team}

    return render(request, 'mainweb/home.html', params)

def gallery(request):
    ima=Gallery.objects.all()
    return render(request, 'mainweb/gallery.html',{'para':ima} )

def about(request):
     
    return render(request,'mainweb/about.html')
def events(request):
    infom=Information.objects.all()
    testi=Testimonianls.objects.all()
    team=Team.objects.all()
    params={'info':infom,'testi':testi,'tea':team}
    return render(request,'mainweb/events.html',params)
