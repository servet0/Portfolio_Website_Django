from django.shortcuts import render
from .models import Navbar, Main

def home(request):
    navbars = Navbar.objects.first()
    mains = Main.objects.all().order_by('date')

    context = {'navbars': navbars, 'mains': mains}

    return render(request, 'base/home.html', context)

# Create your views here.
