from django.shortcuts import render
from .models import Navbar

def home(request):
    navbars = Navbar.objects.first()

    context = {'navbars': navbars,}

    return render(request, 'base/home.html', context)

# Create your views here.
