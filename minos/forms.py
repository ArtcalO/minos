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

class RegisterForm2(forms.ModelForm):
	birthday = forms.DateField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'yyyy-mm-dd ',
				'type':'date'
				}
			)
		)
	inscription_date = forms.DateField(
		widget=forms.TextInput(
			attrs={
				'placeholder':'yyyy-mm-dd ',
				'type':'date'
				}
			)
		)

	class Meta:
		model = Student
		exclude = ['user', 'avatar','niveau','departement','faculty','institut']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['fac'].widget.attrs.update({'class':'radio','type':'radio', 'name':'type'})
		self.fields['inst'].widget.attrs.update({'class':'radio','type':'radio', 'name':'type'})

class RegisterFacForm(forms.ModelForm):

	class Meta:
		model = Student
		fields= ['niveau','departement','faculty']

class RegisterInstForm(forms.ModelForm):

	class Meta:
		model = Student
		fields= ['niveau','institut']

class PayBankForm(forms.ModelForm):
	account_number = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'placeholder':'Numero du compte',
			'type':'text'
			}),label='Numero du compte')
	account_holder = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'placeholder':'Ex : ULT, LAC',
			'type':'text'
			}),label='Nom du compte')
	paid_amount = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'placeholder':'Montant',
			'type':'text'
			}),label='Montant a payer')
	motif = forms.CharField(
		widget=forms.TextInput(
			attrs={
			'placeholder':'motif',
			'type':'text'
			}),label='Motif')
	class Meta:
		model = BankToken
		exclude = ['customer','date', 'token_number']

class AlreadyPayForm(forms.ModelForm):
	num_recu = forms.CharField(
		widget=forms.TextInput(attrs={
			'placeholder':'num_recu',
			'type':'text'
			}))
	montant_paye = forms.CharField(
		widget=forms.TextInput(attrs={
			'placeholder':'montant_paye',
			'type':'text'
			}))
	motif = forms.CharField(
		widget=forms.TextInput(attrs={
			'placeholder':'motif',
			'type':'text'
			}))
	bordereau_blanc = forms.ImageField( widget=forms.FileInput(
			attrs={'placeholder':'Image bordereau blanc','class':'form-control mb-2'}),
		label='bordereau blanc', required=True)

	bordereau_rose = forms.ImageField( widget=forms.FileInput(
			attrs={'placeholder':'Image bordereau rose','class':'form-control mb-2'}),
		label='bordereau rose', required=True)

	date_paye = forms.DateField(
		widget=forms.TextInput(attrs={
			'placeholder':'date',
			'type':'date',
			'class':'form-control'
			}))

	class Meta:
		model = BankTokenPaid
		exclude = ['date', 'student']
