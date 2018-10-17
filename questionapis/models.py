from django.db import models

# Create your models here.


class Question(models.Model):
	ques = models.TextField(max_length=1000,default='No Information')
	option1 = models.TextField(max_length=100,default='No Information')
	option2 = models.TextField(max_length=100,default='No Information')
	option3 = models.TextField(max_length=100,default='No Information')
	option4 = models.TextField(max_length=100,default='No Information')
	difficulty = models.IntegerField(default=1)

	def __str__(self):
		return self.ques