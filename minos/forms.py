from django import forms
from . models import *

class StudentForm(forms.Form):

	first_name= forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Votre nom',
				'type':'text'

				}
			)
		)

	last_name= forms.CharField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'Votre prenom',
				'type':'text'
				}
			)
		)
	email = forms.EmailField(
		widget = forms.TextInput(
			attrs = {
				'placeholder':'Adresse electronique',
				'type':'email'

				}
			)
		)
	password = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'Mot de passe ',
				'type':'password'
				}
			)
		)
	password2 = forms.CharField(
		widget=forms.PasswordInput(
			attrs={
				'placeholder':'Confirmer mot de passe ',
				'type':'password'
				}
			)
		)
	avatar = forms.ImageField(
		widget=forms.FileInput(
			attrs={
				'type':'file'
				}
			)
		)

class ConnexionForm(forms.Form):
    username = forms.CharField(
    	widget=forms.TextInput(
    		attrs={
    			'placeholder':'E-mail',
    			'type':'email'
    			}
    		)
    	)
    password = forms.CharField(
    	widget=forms.PasswordInput(
    		attrs={
    			'placeholder':'Mot de passe ',
    			'type':'password'
    			}
    		)
    	)
