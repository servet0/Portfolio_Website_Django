from django.shortcuts import render, redirect
from .models import Navbar, Main, About, SocialMedia, Footer, Projects, Resume, Experience, Education, Skills, Language, Contact, Policy, ContactName, ProjectName
from .forms import ContactForm

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
    project = Projects.objects.first()
    names = ProjectName.objects.first()

    context = {'navbars': navbars,
               'mains': mains,
               'abouts': abouts,
               'socials': socials,
               'footers': footers,
               'projects': projects,
               'project': project,
               'names': names,
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
    experiences = Experience.objects.all().order_by('-date')
    educations = Education.objects.all().order_by('-date')
    skills = Skills.objects.all().order_by('-date')
    languages = Language.objects.all().order_by('-date')

    context = {'navbars': navbars,
               'mains': mains,
               'abouts': abouts,
               'socials': socials,
               'footers': footers,
               'projects': projects,
               'resume_title': resume_title,
               'resumes': resumes,
               'experiences': experiences,
               'educations': educations,
               'skills': skills,
               'languages': languages,
               }
    
    return render(request, 'base/resume.html', context)

# views.py
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')  # İletişim başarıyla gönderildiyse yönlendir
    else:
        form = ContactForm()

    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')
    abouts = About.objects.all().order_by('date')
    socials = SocialMedia.objects.all().order_by('date')
    footers = Footer.objects.all().order_by('date')
    names = ContactName.objects.first()
    

    context = {'form': form, 
               'navbars': navbars, 
               'mains': mains, 
               'abouts': abouts, 
               'socials': socials, 
               'footers': footers,
               'names': names,
               }

    return render(request, 'base/contact.html', context)

def privacy(request):
    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')
    abouts = About.objects.all().order_by('date')
    socials = SocialMedia.objects.all().order_by('date')
    footers = Footer.objects.all().order_by('date')

    privacies = Policy.objects.first()
    

    context = {'navbars': navbars,
               'mains': mains,
               'abouts': abouts,
               'socials': socials,
               'footers': footers,
               'projects': projects,
               'privacies': privacies,
               }
    
    return render(request, 'base/privacy.html', context)

def terms(request):
    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')
    abouts = About.objects.all().order_by('date')
    socials = SocialMedia.objects.all().order_by('date')
    footers = Footer.objects.all().order_by('date')

    termies = Policy.objects.first()
    

    context = {'navbars': navbars,
               'mains': mains,
               'abouts': abouts,
               'socials': socials,
               'footers': footers,
               'projects': projects,
               'termies': termies,
               }
    
    return render(request, 'base/terms.html', context)

# Create your views here.
