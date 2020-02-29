from django.db import models

# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=250)
	password = models.CharField(max_length=20)
	user_type = models.BooleanField()

	def __str__(self):
		return self.username + ' - ' + str(self.user_type)