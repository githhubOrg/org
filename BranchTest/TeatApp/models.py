from django.db import models

# Create your models here.
class test(models.Model):
    first_num = models.CharField(max_length=20)
    sec_num = models.CharField(max_length=20)
    cal_type = models.CharField(max_length=4)
    cal_result = models.CharField(max_length=20)