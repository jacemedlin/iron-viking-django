from django.db import models

# Create your models here.

class Subscription(models.Model):
	s_name = models.CharField('Subscriber Name',max_length = 40)
	s_email = models.EmailField('Subscriber Email', max_length = 85)
	
	def __str__(self):
		return self.s_name
	