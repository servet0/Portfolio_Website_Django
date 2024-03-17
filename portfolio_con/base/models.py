from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime

class Navbar(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True)
    home = models.CharField(max_length=500, null=True, blank=True)
    resume = models.CharField(max_length=500, null=True, blank=True)
    projects = models.CharField(max_length=500, null=True, blank=True)
    contact = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name = ("Navbar")
        verbose_name_plural = ("Navbardaki Başlıkların İsimleri")

class Main(models.Model):
    tool = RichTextField(null=True, blank=True)
    first_text = RichTextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    resume = models.CharField(max_length=300, null=True, blank=True)
    projects = models.CharField(max_length=300, null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Main")
        verbose_name_plural = ("Anasayfadaki ilk görünen yazılar")

class About(models.Model):
    about = models.CharField(max_length=200, null=True, blank=True)
    me = RichTextField(null=True, blank=True)
    description = RichTextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("About")
        verbose_name_plural = ("Hakkımda")

class SocialMedia(models.Model):
    instagram = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("SocialMedia")
        verbose_name_plural = ("Sosyal Medya")





# Create your models here.
