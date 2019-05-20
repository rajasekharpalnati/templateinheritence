from django.shortcuts import render

def base_page_view(request):
    return render(request,'base1.html')


def home_page_view(request):
    return render(request,'base_home.html')


def home_services_view(request):
    return render(request,'base_services.html')


def home_contact_view(request):
    return render(request,'base_contact.html')


def home_feedback_view(request):
    return render(request,'base_feedback.html')