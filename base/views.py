from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.http import JsonResponse
def home(request):
    sliders=Slider.objects.all()
    services=Service.objects.all()
    consulting_services=ConsultingService.objects.all()
    home_image=HomeImage.objects.last()
    additionals=Additional.objects.all()
    home_service_detail=HomeServiceDetail.objects.last()
    form=ApplyForm()
    if request.method == 'POST':
        form=ApplyForm(request.POST)
        name=request.POST.get('service')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        date=request.POST.get('date')
        print(name)
        service=get_object_or_404(Service, name=name)
        form = Apply(service=service, date=date, email=email, phone=phone)
    
        form.save()
            
    
    return render(request, 'home.html', {'sliders':sliders,'services':services,'additionals':additionals,
                'consulting_services':consulting_services, 'form':form, 'home_image':home_image, 'home_service_detail':home_service_detail})

def about(request):
    services=Service.objects.all()
    about=About.objects.last()
    form=AboutApplyForm()
    home_service_detail=HomeServiceDetail.objects.last()
    if request.method == 'POST':
        form=ApplyForm(request.POST)
        service_name=request.POST.get('service')
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        message=request.POST.get('message')
        print(name)
        service=get_object_or_404(Service, name=service_name)
        form = AboutApply(service=service, name=name,message=message, email=email, phone=phone)
        form.save()
    return render(request, 'about.html', {'services':services,'home_service_detail':home_service_detail, 'about':about, 'form':form})

def services(request):
    services=Service.objects.all()
    return render(request, 'services.html', {'services':services})

def service_detail(request, slug):
    service=get_object_or_404(Service, slug=slug)
    services=Service.objects.all()
    return render(request, 'service_detail.html', {'service':service, 'services':services})

def blog(request):
    blogs=Blog.objects.all()
    return render(request, 'blog.html', {'blogs':blogs})

def blog_detail(request, slug):
    blog=get_object_or_404(Blog, slug=slug)
    blogs=Blog.objects.all()
    return render(request, 'blog_detail.html', {'blog':blog, 'blogs':blogs })

def contact(request):
    form=ContactForm()
    if request.method == 'POST':
        form=ContactForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
           
    return render(request, 'contact.html', {'form':form })