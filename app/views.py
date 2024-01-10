from django.shortcuts import render
from .models import *

def main(request):
    header = Header.objects.all()
    body = Body.objects.all()
    card = Card.objects.all()
    leader = Leader.objects.all()
    leadercards = LeaderCards.objects.all()
    testimonials = Testimonials.objects.all()
    blog = Blog.objects.all()

    context = {
        'header': header,
        'body': body,
        'card': card,
        'leader': leader,
        'leadercards': leadercards,
        'testimonials': testimonials,
        'blog': blog,
    }
    return render(request, 'index.html', context)

def about(request):
    testimonials = Testimonials.objects.all()
    aboutpage = AboutPage.objects.all()
    aboutpagecompany = AboutPageCompany.objects.all()
    context = {
        'testimonials': testimonials,
        'aboutpage': aboutpage,
        'aboutpagecompany': aboutpagecompany,
    }
    return render(request, 'about.html', context)

def blog(request):
    blogpage = Blogpage.objects.all()
    blog = Blog.objects.all()
    context = {
        'blogpage': blogpage,
        'blog': blog,
    }
    return render(request, 'blog.html', context)

def cars(request):
    return render(request, 'cars.html')

def services(request):
    servicespage = ServicesPage.objects.all()
    testimonials = Testimonials.objects.all()
    card = Card.objects.all()
    context = {
        'servicespage': servicespage,
        'card': card,
        'testimonials': testimonials,
    }
    return render(request, 'services.html', context)

def single(request):
    return render(request, 'single.html')
