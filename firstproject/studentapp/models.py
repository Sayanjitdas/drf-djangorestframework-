from django.db import models

# Create your models here.


class Student(models.Model):

    name = models.CharField(verbose_name='Name',max_length=100)
    score = models.DecimalField(verbose_name='Score',max_digits=10,decimal_places=2)

    get_student = models.Manager()

    def __str__(self):
        return self.name