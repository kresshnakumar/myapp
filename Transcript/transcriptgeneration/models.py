from django.db import models

# Create your models here.
class Student(models.Model):
	SID = models.CharField(max_length = 15)
	firstname = models.CharField(max_length = 30)
	lastname = models.CharField(max_length = 30)
	emailid = models.CharField(max_length = 50)
	phnum = models.CharField(max_length = 15)
	yearofjoining = models.IntegerField(default = 0)
	yearofpassing = models.IntegerField(default = 0)
	batch = models.IntegerField(default = 0)