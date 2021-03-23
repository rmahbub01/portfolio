import json
import os

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render

from .models import *

# Create your views here.
pwd = os.path.dirname(__file__)
config_dir = open(pwd + '/config.json','r')
params = json.loads(config_dir.read())['params']

def homePageView(request):
    models = {
        "abouts":About.objects.all(),
        "facts":Facts.objects.all(),
        "skills": Skill.objects.all(),
        "summary":Summary.objects.all(),
        "experiences":Experience.objects.all(),
        "educations":Education.objects.all(),
        "portfolios":Portfolio.objects.all(),
        "services":Service.objects.all(),
        "testimonials":Testimonial.objects.all(),
        'contacts':Contact.objects.all(),
        'params':params
    }

    if request.method == 'POST':
        contact = Email_Contact()
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse('Thanks for Contact me...')


    return render(request, 'index.html',context=models)
