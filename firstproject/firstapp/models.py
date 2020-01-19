from django.db import models

# Create your models here.
class EmployeeModel(models.Model):

    name  = models.CharField(max_length=100,verbose_name='Name')
    salary = models.FloatField(verbose_name='Salary')

    get_emp = models.Manager()

    def __str__(self):
        return self.name