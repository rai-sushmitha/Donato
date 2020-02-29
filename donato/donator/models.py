from django.db import models

# Create your models here.
class Donations(models.Model):
	Title = models.CharField(max_length=100)
	Donation = models.CharField(max_length=50)

	def __str__(self):
		return self.Title + ' - ' + self.Donation