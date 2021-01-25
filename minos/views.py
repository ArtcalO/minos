from django.views import View
from . forms import *
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

@login_required(login_url='/connexion/')
def home(request):
	txt = "<h1>Connected</h1>"
	return render(request, 'home.html', locals())

def connexion(request):
	login_form = ConnexionForm(request.POST)
	try:
		next_p = request.GET["next"]
	except:
		next_p = ""
	if request.method == "POST" and login_form.is_valid():
		username = login_form.cleaned_data['username']
		password = login_form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user:  # Si l'objet renvoyé n'est pas None
			login(request, user)
			if next_p:
				return redirect(next_p)
			else:
				return redirect(home)
	login_form = ConnexionForm()
	return render(request, 'login.html', locals())

def deconnexion(request):
	logout(request)
	return redirect(connexion)

def register(request):
	if request.method == "POST" :
		register_form = StudentForm(request.POST, request.FILES)
		if register_form.is_valid():
			first_name = register_form.cleaned_data['first_name']
			last_name = register_form.cleaned_data['last_name']
			password = register_form.cleaned_data['password']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			avatar = register_form.cleaned_data['avatar']
			if password==password2:
				user = User.objects.create_user(
					username=email, 
					email=email, 
					password=password)
				user.first_name, user.last_name = first_name, last_name
				user.save()
				Student(user=user, avatar=avatar).save()
		if user:
			login(request, user)
			return redirect(home)
	register_form = StudentForm()
	return render(request, 'register.html', locals())
