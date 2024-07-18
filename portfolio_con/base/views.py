from django.shortcuts import render
from .models import Navbar, Main, About, SocialMedia, Footer, Projects, Resume

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
    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')
    abouts = About.objects.all().order_by('date')
    socials = SocialMedia.objects.all().order_by('date')
    footers = Footer.objects.all().order_by('date')
    projects = Projects.objects.all().order_by('-date')

    context = {'navbars': navbars,
               'mains': mains,
               'abouts': abouts,
               'socials': socials,
               'footers': footers,
               'projects': projects,
               }

    return render(request, 'base/projects.html', context)

def resume(request):
    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')
    abouts = About.objects.all().order_by('date')
    socials = SocialMedia.objects.all().order_by('date')
    footers = Footer.objects.all().order_by('date')
    projects = Projects.objects.all().order_by('-date')
    resume_title = Resume.objects.first()
    resumes = Resume.objects.all().order_by('-date')

    context = {'navbars': navbars,
               'mains': mains,
               'abouts': abouts,
               'socials': socials,
               'footers': footers,
               'projects': projects,
               'resume_title': resume_title,
               'resumes': resumes,
               }
    
    return render(request, 'base/resume.html', context)

# Create your views here.
