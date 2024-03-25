from django.shortcuts import render
from .models import Navbar, Main, About, SocialMedia, Footer, Projects

def home(request):
    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')
    abouts = About.objects.all().order_by('date')
    socials = SocialMedia.objects.all().order_by('date')
    footers = Footer.objects.all().order_by('date')

    context = {'navbars': navbars,
               'mains': mains,
               'abouts': abouts,
               'socials': socials,
               'footers': footers}

    return render(request, 'base/home.html', context)

def projects(request):
    projects = Projects.objects.all().order_by('-date')

    context = {
        'projects': projects,
    }

    return render(request, 'base/projects.html', context)

# Create your views here.
