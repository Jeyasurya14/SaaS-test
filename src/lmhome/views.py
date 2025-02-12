from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisits
def page_visits(request, *args, **kwargs):
    return about_visits(request, *args, **kwargs)

def about_visits(request, *args, **kwargs):
    Total_visits = PageVisits.objects.all()
    page_visit = PageVisits.objects.filter(path=request.path)

    html = 'main.html'
    visits_data = {
        'Total_visits': Total_visits.count(),
        'page_visit': page_visit.count(),
    }
    PageVisits.objects.create(path=request.path)
    return render(request, html, visits_data )