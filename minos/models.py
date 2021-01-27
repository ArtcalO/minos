from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone	

NIVEAU = ((1,'Bac I'), (2,"Bac II"), (3,'Bac II'))
GENDERS = (("H", 'Homme'), ("F", "Femme"))

class Minerval(models.Model):
	amount = models.FloatField()
	academic_year = models.CharField(max_length=100)
	faculty = models.ForeignKey("Faculty", on_delete=models.CASCADE)

class Faculty(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class Institut(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name
		
class Departement(models.Model):
	name = models.CharField(max_length=100)
	faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.name} - {self.faculty.name}"


class Comptable(models.Model):
	user = models.OneToOneField(User, null=True, verbose_name='Comptable' ,unique=True,on_delete=models.CASCADE)
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/comptables/")
	matricule = models.IntegerField(null=True, blank=True)
	birthday = models.DateField(null=True, blank=True, max_length=100)

	def __str__(self):
		return f"{self.user.username} - {self.matricule} "

class Student(models.Model):
	user = models.OneToOneField(User, null=True, unique=True,on_delete=models.CASCADE)
	matricule = models.IntegerField(null=True, blank=True)
	birthday = models.DateField(null=True, blank=True, max_length=100)
	academic_year = models.CharField(blank=True, null=True, max_length=50)
	inscription_date = models.DateField(blank=True, null=True)
	niveau = models.PositiveIntegerField(choices=NIVEAU, null=True)
	genre = models.CharField(max_length=5, choices=GENDERS, null=True)
	departement = models.ForeignKey(Departement, blank=True, null=True, on_delete=models.CASCADE)
	faculty = models.ForeignKey(Faculty, blank=True, null=True, on_delete=models.CASCADE)
	institut = models.ForeignKey(Institut, blank=True, null=True, on_delete=models.CASCADE)
	fac = models.BooleanField(null=True)
	inst = models.BooleanField(null=True)
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/students/")

	def __str__(self):
		return f"{self.user.username}"

	def verifyStep1(self):
		if (self.matricule!= None and
			self.inscription_date!= None and
			self.academic_year != None and
			self.genre !=None and
			self.birthday != None):
			return True

	def verifyFac(self):
		if(self.niveau != None and self.faculty!=None):
			return True

	def verifyInst(self):
		if(self.niveau != None and sefl.institut != None):
			return True

class Bank(models.Model):
	name = models.CharField(max_length=30)
	capital = models.FloatField()
	head_quarter = models.CharField(max_length=50)
	postal = models.CharField(max_length=100)
	phone = models.CharField(max_length=50)
	site_web = models.CharField(max_length=100)

	def __str__(self):
		return f"{self.name}-{self.capital} - {self.head_quarter}"


class BankToken(models.Model):
	bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
	token_number = models.IntegerField()
	account_number = models.IntegerField()
	account_holder = models.CharField(max_length=20, default="ULT")
	customer = models.ForeignKey(User, on_delete=models.CASCADE)
	paid_amount = models.FloatField()
	motif = models.CharField(max_length=50)
	date = models.DateField(default=timezone.now)

	def __str__(self):
		return f"{self.token_number} by {self.customer.user.username} - {self.paid_amount} "


class HistoryBankToken(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	bank_token = models.ForeignKey(BankToken, on_delete=models.CASCADE)
	date = models.DateField()

class UltToken(models.Model):
	token_number = models.IntegerField()
	token_bank_number = models.IntegerField()
	date = models.DateField(default=timezone.now)
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	amount_paid_ult = models.FloatField()
	motif = models.CharField(max_length=50)

	def __str__(self):
		return f"{self.student.user.username} - {self.amount_paid_ult} "

class AlreadyPaidStudent(models.Model):
	student = models.ForeignKey(User, on_delete=models.CASCADE)
	paid_already = models.FloatField()
	remain = models.FloatField(default=0)
	total_to_pay = models.ForeignKey(Minerval, on_delete=models.CASCADE)
	tranche_1 = models.BooleanField(False)
	tranche_2 = models.BooleanField(False)
	tranche_3 = models.BooleanField(False)
	tranche_4 = models.BooleanField(False)
	validated = models.BooleanField(False)

	def __str__(self):
		return f"{self.student.user.username} Paid :{self.paid_already} Remain :{self.remain}"



	
		