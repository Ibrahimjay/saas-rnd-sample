from django.http import HttpResponse
from django.shortcuts import render
from visits.models import page_visit

def home_page(request):
    my_title = "My Page"
    my_contex = {
        'page_title': my_title
    }

    page_visit.objects.create()
    return render(request, 'home.html', my_contex)