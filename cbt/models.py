from django.db import models

# Create your models here.

class UserRegistration(models.Model):
	#usedID=models.CharField(max_length=25,primary_key=True)
	username=models.CharField(max_length=20)
	emailID=models.EmailField(max_length=25)
	password1=models.CharField(max_length=20)
	#password2=models.CharField(max_length=20)
	def __str__(self):
		return self.username
	class Meta:
		ordering=['username']

