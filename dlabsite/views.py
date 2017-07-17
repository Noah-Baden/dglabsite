from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import (lab_member, research, publication, job_listing,
    current_study, data_listing, software_listing)
from datetime import datetime

# homepage
def home_page(request):
    return render(request, 'dlabsite/index.html')

# lab member page
def people_page(request):
    # Get all lab members
    members = lab_member.objects.all().order_by('last_name')
    return render(request, 'dlabsite/people.html', {'members': members})

# research
def research_page(request):
    query_research = research.objects.all()
    return render(request, 'dlabsite/research.html', {'query_research': query_research})

# publications
def publications_page(request):
    publications = publication.objects.all().order_by('-date')
    lastfiveyears = [datetime.now().year,datetime.now().year-1,datetime.now().year-2,datetime.now().year-3,datetime.now().year-4]
    return render(request, 'dlabsite/publications.html', {'publications': publications,'lastfiveyears': lastfiveyears})

# data
def data_page(request):
    data = data_listing.objects.all().order_by('title')
    return render(request, 'dlabsite/data.html', {'data': data})

# software
def software_page(request):
    software = software_listing.objects.all().order_by('title')
    return render(request, 'dlabsite/software.html', {'software': software})

# wiki
def wiki_page(request):
    return HttpResponseRedirect('http://10.20.94.224:778/')

# directions
def directions_page(request):
    return render(request, 'dlabsite/directions.html')

# participate
def participate_page(request):
    currentstudies = current_study.objects.all().order_by('title')
    return render(request, 'dlabsite/participate.html', {'currentstudies': currentstudies})

# careers
def careers_page(request):
    jobpostings = job_listing.objects.all().order_by('-post_date')
    return render(request, 'dlabsite/careers.html', {'jobpostings': jobpostings})

# contact
def contact_page(request):
    return render(request, 'dlabsite/contact.html')
