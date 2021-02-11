from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Personnel(models.Model):
	user = models.OneToOneField(User, null=True, verbose_name='Personnel' ,unique=True,on_delete=models.CASCADE)
	avatar = models.ImageField(null=True, blank=True, upload_to="avatars/comptables/")
	matricule = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return f"{self.user.username} - {self.matricule} "
