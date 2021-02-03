from django.db import models


# Create your models here.

class Employee(models.Model):  
	eid = models.CharField(max_length=20)
	ename = models.CharField(max_length=100)
	econtact = models.CharField(max_length=15)

	class Meta:
		db_table = "employee"

    # first_name = models.CharField(max_length=20)  
    # last_name = models.CharField(max_length=20)
    # contact = models.IntegerField()
    # email = models.EmailField(max_length=20)
    # age = models.IntegerField()
    