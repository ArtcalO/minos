from django.views import View
from . forms import *
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render,redirect
def home(request):
	txt = "hey brother"
	return render(request, 'home.html', locals())

def register(request):
	register_form = studentForm(request.POST or None, request.FILES)
	if request.method == "POST" :
		if register_form.is_valid():
			username = register_form.cleaned_data['username']
			print('rrrrrrrrrrrrrrr')
			print(username)
			print('rrrrrrrrrrrrrrrr')
			first_name = register_form.cleaned_data['first_name']
			last_name = register_form.cleaned_data['last_name']
			password = register_form.cleaned_data['password']
			password2 = register_form.cleaned_data['password2']
			email = register_form.cleaned_data['email']
			avatar = register_form.cleaned_data['avatar']
			matricule = register_form.cleaned_data['matricule']
			birthday = register_form.cleaned_data['birthday']
			inscription_date = register_form.cleaned_data['inscription_date']
			if password==password2:
				try:
					user = User.objects.create_user(
						username=username,password=password)
					print(user)
					user.first_name=first_name
					user.last_name=last_name
					user.email=email
					user.save()
					Student(user=user, avatar=avatar,matricule = matricule,birthday = birthday,inscription_date = inscription_date).save()
					if user:
						login(request, user)
						return redirect('home')
				except Exception as e:
					messages.error(request, "name Already exit")
	register_form = studentForm()
	return render(request, 'register.html', locals())