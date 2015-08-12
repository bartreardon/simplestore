from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    testing_yo = forms.CharField(label='Just a test', max_length=100)
    
class BuyForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    testing_yo = forms.CharField(label='Just a test', max_length=100)