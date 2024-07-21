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

class Footer(models.Model):
    copyright = models.CharField(max_length=400, null=True, blank=True)
    copyright_text = models.TextField(null=True, blank=True)
    privacy = models.TextField(null=True, blank=True)
    terms = models.TextField(null=True, blank=True)
    contact = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Footer")
        verbose_name_plural = ("Footer")

class Projects(models.Model):
    title = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='project_image')
    url = models.URLField(null=True, blank=True, verbose_name="Proje linki")

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Projects")
        verbose_name_plural = ("Projeler")

class Resume(models.Model):
    title_resume = models.CharField(max_length=300, null=True, blank=True)
    title_experience = models.CharField(max_length=300, null=True, blank=True)
    title_education = models.CharField(max_length=300, null=True, blank=True) 
    title_skills = models.CharField(max_length=500, null=True, blank=True)
    title_languages = models.CharField(max_length=500, null=True, blank=True)
    
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Resume")
        verbose_name_plural = ("Özgeçmiş")

class Experience(models.Model):
    date_experience = models.CharField(max_length=500, null=True, blank=True)
    company_experience = models.CharField(max_length=700, null=True, blank=True)
    location_experience = models.CharField(max_length=700, null=True, blank=True)
    description_experience = RichTextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Experience")
        verbose_name_plural = ("Deneyim")

class Education(models.Model):
    date_education = models.CharField(max_length=500, null=True, blank=True)
    school_education = models.CharField(max_length=700, null=True, blank=True)
    location_education = models.CharField(max_length=700, null=True, blank=True)
    departman_education = models.CharField(max_length=1000, null=True, blank=True)
    description_education = RichTextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Education")
        verbose_name_plural = ("Eğitim")

class Skills(models.Model):
    text1_skills = models.TextField(null=True, blank=True)
    text2_skills = models.TextField(null=True, blank=True)
    text3_skills = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Skills")
        verbose_name_plural = ("Yetenekler")

class Language(models.Model):
    text1_languages = models.TextField(null=True, blank=True)
    text2_languages = models.TextField(null=True, blank=True)
    text3_languages = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Language")
        verbose_name_plural = ("Diller")

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField(max_length=11)
    message = models.TextField()
    
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Contact")
        verbose_name_plural = ("İletişim")

class Policy(models.Model):
    privacy = RichTextField(null=True, blank=True)
    terms = RichTextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("Policy")
        verbose_name_plural = ("Privacy metni")

class ContactName(models.Model):
    name = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("ContactName")
        verbose_name_plural = ("İletişim sayfasının başındaki yazı")

class ProjectName(models.Model):
    name = models.TextField(null=True, blank=True)

    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = ("ProjectName")
        verbose_name_plural = ("Proje sayfasının altındaki yazı")





# Create your models here.
