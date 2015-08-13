from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.shortcuts import render

from .models import Apps, Purchases
from .forms import NameForm, BuyForm

import datetime

def index(request):
    return HttpResponse("Hello, world.")
    
def applist(request):
	applications = Apps.objects.all()
	data = serializers.serialize('json', applications)

	return HttpResponse(data, content_type='application/json')
	
def purchased_apps(request):
	
	# change to whatever username you need or use some kind of auth
	username = "bart"
	#username = request.user
	
	purchases = Apps.objects.filter(purchases__user=username)
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
    
    
def get_name(request, **kwargs):

    appName = request.GET.get('appName', '')
    userName = request.GET.get('userName', '')
    form = BuyForm(initial={'appName': appName, 'user': userName, 'purchase_date': datetime.datetime.now()})
		
    return render(request, 'purchase.html', {'form': form})
    
def buy_app(request):
    errors = []
    if request.method == 'POST':
    
        form = BuyForm(request.POST)
        if form.is_valid():
        	
        	purchasedApp = form.save(commit=False)
        	
        	appName = form.data['appName']
        	appObject = Apps.objects.get(app_name=appName)
        	appNameKey = appObject.id
        	#form.instance.purchased_app = Apps.objects.filter(purchases__purchased_app=appName)
        	#form.data['purchased_app'] = appNameKey
        	purchasedApp.purchased_app = appNameKey
        	
        	
        	purchasedApp.save()
        	return HttpResponseRedirect('/contact/thanks/')
            #appName = form.cleaned_data['appName']
            #userName = form.cleaned_data['userName']
            #costCode = form.cleaned_data['costCode']

            #purchases = Apps.objects.create(
            #    purchases__app=appName,
            #    user=userName,
            #    purchase_date=datetime.datetime.now(),
            #    cost_code=costCode,)
    	
        #if not request.POST.get('appName', ''):
        #    errors.append('enter an application name.')
        #if not request.POST.get('userName', ''):
        #    errors.append('Enter your name')
        #if not request.POST.get('costCode'):
        #    errors.append('Enter a  cost code.')
        #if not errors:
            # write to the DB or something
        #    appName = request.POST.get('appName', '')
        #    userName = request.POST.get('userName', '')
        #    costCode = request.POST.get('costCode')
            
            
        return HttpResponseRedirect('/contact/thanks/')
    return render(request, 'contact_form.html',
        {'errors': errors})


# ----------------------------
    