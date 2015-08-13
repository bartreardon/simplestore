from django import forms
from django.forms import ModelForm
from .models import Apps, Purchases

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    testing_yo = forms.CharField(label='Just a test', max_length=100)
    
#class BuyForm(forms.Form):
#    userName = forms.CharField(label='Your name', max_length=100)
#    appName = forms.CharField(label='App name', max_length=100)
#    costCode = forms.CharField(label='Cost Code', max_length=20)
    
class BuyForm(ModelForm):
	class Meta:
		model = Purchases
		#purchasedApp = forms.ModelChoiceField(queryset=Apps.objects.filter(purchased_app=appName)
		#self.fields['']
		exclude = ("purchased_app",)
		#fields = ['user', 'purchase_date', 'cost_code']
		
		#purchases__user=username