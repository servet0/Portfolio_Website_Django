from django.shortcuts import render
from .models import Navbar, Main, About

def home(request):
    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')
    abouts = About.objects.all().order_by('date')
    socials = About.objects.all().order_by('date')

    context = {'navbars': navbars, 'mains': mains, 'abouts': abouts, 'socials': socials}

    return render(request, 'base/home.html', context)

# Create your views here.
