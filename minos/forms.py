from django import forms
from . models import *

class studentForm(forms.Form):
	username=forms.CharField(max_length=20)
	first_name=forms.CharField(max_length=20)
	last_name=forms.CharField(max_length=20)
	email=forms.EmailField(max_length=20)
	password=forms.CharField(max_length=20, widget=forms.PasswordInput)
	password1=forms.CharField(max_length=20, widget=forms.PasswordInput)
	#--------------------#
	avatar = forms.ImageField()
	matricule = forms.IntegerField()
	birthday = forms.DateField(widget = forms.DateInput(
	        attrs={
	            'type':'date',
	        }
	    ))
	inscription_date = forms.DateField(widget = forms.DateInput(
	        attrs={
	            'type':'date',
	        }
	    ))