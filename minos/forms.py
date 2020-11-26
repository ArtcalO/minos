from django import forms
from .models import *
from django.contrib.auth.models import User
from datetime import date

FACULTIES = [
	('info', 'INFO'),
	('economie', 'ECONOMIE'),
	('statistique', 'STATISTIQUE'),
	('science po', 'SCIENCE PO'),
]

TRIM_CHOICES = [
	('1tr', '1èr Tranche'),
	('2tr', '2ème Tranche'),
	('3tr', '3ème Tranche'),
	('4tr', '4ème Tranche'),
]

class StudentForm(forms.Form):
	firstname = forms.CharField(label='First name')
	lastname = forms.CharField(label='Last name')
	username = forms.CharField(label='Username')
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ',}), label='Password')
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password ',}), label='Confirmer')
	email = forms.EmailField(label='Email address')
	avatar = forms.ImageField(label='Avatar')
	matricule = forms.IntegerField(label='Matricule')
	faculty = forms.ChoiceField(
		required=True,
        widget=forms.Select,
        choices=FACULTIES,
		)
	birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            years=range(1960, date.today().year),
            ),
        label='Date naissance')
	academic_year = forms.CharField(label='Année-Academique')


class ConnexionForm(forms.Form):
	username = forms.CharField(label='Username')
	password = forms.CharField( widget=forms.PasswordInput(attrs={'placeholder':'Password ',}), label='Password')

class BankTokenForm(forms.ModelForm):
	motif = forms.ChoiceField(
		required=True,
        widget=forms.Select,
        choices=TRIM_CHOICES,
		)
	class Meta:
		model = BankToken
		exclude = ['customer', 'date','token_number',]

