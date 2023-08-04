from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Slider(models.Model):
    title=models.CharField(max_length=50)
    text=models.CharField(max_length=80)
    image=models.ImageField()
    def __str__(self):
        return self.title
    
class Map(models.Model):
    link=models.TextField()
    
class Service(models.Model):
    slug=models.SlugField(null=True, unique=True)
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
    
    @property
    def get_absolute_url(self):
        return reverse("service_detail", kwargs={"slug": self.slug})
class Blog(models.Model):
    slug=models.SlugField(null=True, unique=True)
    title=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    @property
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})
    
class Contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    subject=models.CharField(max_length=100)
    message=models.TextField()
    def __str__(self):
        return f'{self.name, self.email}'

class BackgroundImage(models.Model):
    about=models.ImageField(_("Haqqimizda arxa plan sekil"),null=True, blank=True)
    services=models.ImageField(_("Xidmetler arxa plan sekil"),null=True, blank=True)
    blogs=models.ImageField(_("Bloq arxa plan sekil"),null=True, blank=True)
    class Meta:
        verbose_name_plural = "Arxa plan sekilleri"


class Main(models.Model):
    header_logo=models.ImageField(null=True, blank=True)
    footer_logo=models.ImageField(null=True, blank=True)
    footer_text=models.TextField()
    footer_image=models.ImageField(null=True, blank=True)
    apply_image=models.ImageField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Esas Melumatlar"

class MainContact(models.Model):
    main=models.ForeignKey(Main,  on_delete=models.SET_NULL, null=True, blank=True, related_name='main_contact' )
    address=models.CharField(max_length=100, null=True, blank=True)
    email=models.EmailField(max_length=70, null=True, blank=True)
    phone=models.CharField(max_length=20, null=True, blank=True)

class OpeningHours(models.Model):
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100, null=True)

class About(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    image=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title

class AboutDetailed(models.Model):
    detail=models.ForeignKey(About,  on_delete=models.SET_NULL, null=True, blank=True, related_name='about_details' )
    image=models.TextField()
    title=models.CharField(max_length=100)
    text=models.TextField()
class HomeServiceDetail(models.Model):
    text=models.TextField()

class ConsultingService(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image=models.TextField()
    def __str__(self):
        self.title
class HomeImage(models.Model):
    image=models.ImageField(null=True, blank=True)

class Additional(models.Model):
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image=models.TextField()
    def __str__(self):
        self.title
class Apply(models.Model):
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    service=models.ForeignKey(Service, on_delete= models.CASCADE, null=True)
    date=models.CharField(max_length=50)

class AboutApply(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=30)
    service=models.ForeignKey(Service, on_delete= models.CASCADE, null=True)
    message=models.TextField()
    def __str__(self):
        return f'{self.name, self.service}'

class Subscribe(models.Model):
    email=models.EmailField()
    def __str__(self):
        return self.email
class SocialMedia(models.Model):
    class SocialChoices(models.TextChoices):
        INSTAGRAM = "insta", "Instagram"
        FACEBOOK = "fb", "Facebook"
        WHATSAPP = "wp", "Whatsapp"
      
    app=models.CharField(max_length=100, choices=SocialChoices.choices)
    link=models.TextField(null=True)
    def __str__(self):
        return self.app