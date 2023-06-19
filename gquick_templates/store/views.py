from django.shortcuts import render

# Create your views here.


def banner_section(request):
    return render(request, 'home/banner-section/banner-section.html')


def banner_section_mobile(request):
    return render(request, 'home/banner-section/banner-section-mobile.html')
