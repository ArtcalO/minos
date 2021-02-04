from django.views import View
from . forms import *
from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

def randNumber(x):
	return x+1

@login_required(login_url='/connexion/')
def home(request):
	student = Student.objects.get(user=request.user)
	if ((student.verifyStep1() and student.verifyFac()) or (student.verifyStep1() and student.verifyFac())):
		bank_pay_form = PayBankForm(request.POST or None)
		already_paid_form = AlreadyPayForm(request.POST or None, request.FILES)
		if "payer" in request.POST:
			if request.method == 'POST' and bank_pay_form.is_valid():
				pay_form = bank_pay_form.save(commit=False)
				try:
					y = BankToken.objects.all().last()
					x = y.token_number
					pay_form.token_number = randNumber(x)
				except :
					pay_form.token_number = 1

				pay_form.customer = request.user
				pay_form.save()
				UltHistoryBankToken(bank_token = pay_form).save()
			bank_pay_form = PayBankForm()
		if "deja_paye" in request.POST:
			if request.method =="POST" and already_paid_form.is_valid():
				paid_form = already_paid_form.save(commit=False)
				paid_form.student = request.user
				paid_form.save()
			already_paid_form = AlreadyPayForm(request.FILES)
		return render(request, 'home.html', locals())
	else:
		return redirect(register)

@login_required(login_url='/connexion/')
def validated(request):
	validated = True
	student = Student.objects.get(user=request.user)
	return render(request, 'payements.html', locals())

@login_required(login_url='/connexion/')
def information(request):
	information = True
	student = Student.objects.get(user=request.user)
	return render(request, 'payements.html', locals())

@login_required(login_url='/connexion/')
def pending(request):
	pending = True
	student = Student.objects.get(user=request.user)
	return render(request, 'payements.html', locals())

@login_required(login_url='/connexion/')
def errors(request):
	errors = True
	student = Student.objects.get(user=request.user)
	return render(request, 'payements.html', locals())

@login_required(login_url='/connexion/')
def payements(request):
	payements=True
	student = Student.objects.get(user=request.user)
	return render(request, 'payements.html', locals())

@login_required(login_url='/connexion/')
def register2(request):

	if(request.user):
		student = Student.objects.get(user=request.user)
		profil_form = RegisterForm2(request.POST, request.FILES, instance=student)
		if request.method == "POST":
			if(profil_form.is_valid()):
				fac = profil_form.cleaned_data['fac']
				inst = profil_form.cleaned_data['inst']
				profil_form.save()
				print(fac)
				print(inst)
				if fac:
					return redirect(registerFac)
				else:
					return redirect(registerInst)
		else:
			profil_form = RegisterForm2(instance=student)
		return render(request, 'register2.html', locals())
	else:
		return redirect(register)

@login_required(login_url='/connexion/')
def registerFac(request):
	student = Student.objects.get(user=request.user)
	if(student.verifyStep1()):
		profil_form = RegisterFacForm(request.POST, request.FILES, instance=student)
		if request.method == "POST":
			if(profil_form.is_valid()):
				print(profil_form)
				profil_form.save()
			return redirect(home)
		else:
			profil_form = RegisterFacForm(instance=student)
		return render(request, 'register_fac.html', locals())
	else:
		return redirect(register2)

@login_required(login_url='/connexion/')
def registerInst(request):
	student = Student.objects.get(user=request.user)
	if student.verifyStep1():
		profil_form = RegisterInstForm(request.POST, request.FILES, instance=student)
		if request.method == "POST":
			if(profil_form.is_valid()):
				print(profil_form)
				profil_form.save()
			return redirect(home)
		else:
			profil_form = RegisterInstForm(instance=student)
		return render(request, 'register_inst.html', locals())
	else:
		return redirect(register2)


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
			return redirect(register2)
	register_form = StudentForm()
	return render(request, 'register.html', locals())

