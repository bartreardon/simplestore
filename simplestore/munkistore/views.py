from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render

from .models import Apps, Purchases
from .forms import NameForm

import datetime

def index(request):
    return HttpResponse("Hello, world.")
    
def applist(request):
	applications = Apps.objects.all()
	data = serializers.serialize('json', applications)

	return HttpResponse(data, content_type='application/json')
	
def purchased_apps(request):
	username = request.user
	#purchases = Purchases.objects.filter(user="%s" % username)
	purchases = Apps.objects.filter(purchases__user="bart")
	data = serializers.serialize('json', purchases)

	return HttpResponse(data, content_type='application/json')
    
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    
def usertest(request):
    username = request.user
    html = "<html><body>You are %s.</body></html>" % username
    return HttpResponse(html)
    
    
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = request.GET.get('name', '')
            return HttpResponse("Hello %s" % name)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        name = request.GET.get('name', '')
		
    return render(request, 'name.html', {'form': form})
    
def buy(request):
    errors = []
    if request.method == 'POST':
        if not request.POST.get('app_name', ''):
            errors.append('enter an application name.')
        if not request.POST.get('name', ''):
            errors.append('Enter your name')
        if request.POST.get('cost_code'):
            errors.append('Enter a  cost code.')
        if not errors:
            # write to the DB or something
            return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html',
        {'errors': errors})


# ----------------------------
    