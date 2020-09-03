from django.db import models
from django.urls import reverse

class Car(models.Model):
	make = models.CharField(max_length=120)
	model = models.CharField(max_length=120)
	year = models.IntegerField()
	img = models.ImageField(null=True, blank=True)

	def __str__(self):
		return "{} {} - {}".format(self.make, self.model, self.year)

	def get_absolute_url(self):
		return reverse('car-detail', kwargs={'car_id':self.id})
