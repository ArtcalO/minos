from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

START_TOKEN_NUMBER_BANK = 2600.0
START_TOKEN_NUMBER_ULT = 3600.0

@login_required
def getPercent(amount, total):
	return amount*100/total
@login_required
def getRemain(paid, total):
	return total-paid

def home(request):
	return render(request, 'home.html', locals())

def vue(request):
	current_std = Student.objects.get(user=request.user)
	paid = PaidStudent.objects.filter(student=current_std)
	return render(request, 'vue.html', locals())	

def connexion(request):
    error = False

    if request.method == "POST":
        connexion_form = ConnexionForm(request.POST)
        if connexion_form.is_valid():
            username = connexion_form.cleaned_data["username"]
            password = connexion_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect(home)
            else:
                error = True
    else:
        connexion_form = ConnexionForm()
    return render(request, 'forms.html', locals())

def inscription(request):
	if(request.method == 'POST'):
		student_form = StudentForm(request.POST or None, request.FILES)
		if(student_form.is_valid()):
			username = student_form.cleaned_data['username']
			password = student_form.cleaned_data['password']
			firstname = student_form.cleaned_data['firstname']
			lastname = student_form.cleaned_data['lastname'] 
			password2 = student_form.cleaned_data['password2']
			email = student_form.cleaned_data['email']
			avatar = student_form.cleaned_data['avatar']
			matricule = student_form.cleaned_data['matricule']
			faculty = student_form.cleaned_data['faculty']
			birthday = student_form.cleaned_data['birthday']
			academic_year = student_form.cleaned_data['academic_year']

			if(password == password2):
				user = User.objects.create_user(username = username, password=password)
				user.first_name = firstname
				user.last_name = lastname
				user.email =email
				user.save()

				print(user)

				std = Student(user = user,
								avatar=avatar,
								matricule=matricule,
								faculty=faculty,
								birthday=birthday,
								academic_year=academic_year ).save()
				if user: 
					login(request, user)
					return redirect(home)  
				else:
					return redirect(connexion)
			else:
				student_form = StudentForm(request.FILES)

	student_form = StudentForm(request.FILES)
	return render(request, 'forms.html', locals())

@login_required
def payement(request):
	token_form = BankTokenForm(request.POST)
	current_student = Student.objects.get(user=request.user)
	if request.method == "POST":
		if token_form.is_valid():
			try:
				# Inserting into BankToken
				cc = BankToken.objects.all().count()
				last_token_bank = BankToken.objects.all()[cc]
				pay_std = token_form.save(commit=False)
				pay_std.token_number = last_token_bank.token_number+1
				pay_std.customer = current_student
				pay_std.save()

				# Inserting into Ult Token
				cb = UltToken.objects.all().count()
				last_token_ult = UltToken.objects.all()[cb]
				obj = UltToken(token_number = last_token_ult.token_number,
								token_bank_number = pay_std.token_number,
								student = current_student,
								amount_paid_ult = pay_std.amount_paid_bank,
								motif = pay_std.motif).save()
				#Inserting into PaidStudent

				std_paid = PaidStudent.objects.get(student=current_student)
				std_paid.paid_already += pay_std.amount_paid_bank
				std_paid.remain -= pay_std.amount_paid_bank
				std_paid.percent = getPercent(std_paid.paid_already, std_paid.total_to_pay)
				if pay_std.motif == "1tr":
					std_paid.tranche_1 = True

				if pay_std.motif == "2tr":
					std_paid.tranche_2 = True

				if pay_std.motif == "3tr":
					std_paid.tranche_3 = True

				if pay_std.motif == "4tr":
					std_paid.tranche_4 = True

				if (std_paid.tranche_1 == True &
					std_paid.tranche_2 == True &
					std_paid.tranche_3 == True &
					std_paid.tranche_4 == True):
						std_paid.validated = True

				std_paid.save()
				return redirect(home)

			except :

				pay_std = token_form.save(commit=False)
				pay_std.token_number = START_TOKEN_NUMBER_BANK
				pay_std.customer = current_student
				pay_std.save()

				obj = UltToken(token_number = START_TOKEN_NUMBER_ULT,
								token_bank_number = pay_std.token_number,
								student = current_student,
								amount_paid_ult = pay_std.amount_paid_bank,
								motif = pay_std.motif)
				obj.save()

				std_paid = PaidStudent(student=current_student,
										paid_already = pay_std.amount_paid_bank,
										remain = getRemain(pay_std.amount_paid_bank, TOTAL),
										percent = getPercent(std_paid.paid_already, std_paid.total_to_pay))

				if pay_std.motif == "1tr":
					std_paid.tranche_1 = True

				if pay_std.motif == "2tr":
					std_paid.tranche_2 = True

				if pay_std.motif == "3tr":
					std_paid.tranche_3 = True

				if pay_std.motif == "4tr":
					std_paid.tranche_4 = True

				if (std_paid.tranche_1 == True &
					std_paid.tranche_2 == True &
					std_paid.tranche_3 == True &
					std_paid.tranche_4 == True):
						std_paid.validated = True

				std_paid.save()
				return redirect(home)
		else:
			token_form = BankTokenForm(request.FILES)
	token_form = BankTokenForm()	
	return render(request, 'forms.html',locals())

def deconnexion(request):
	logout(request)
	return redirect(home)
