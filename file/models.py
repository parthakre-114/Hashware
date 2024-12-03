
from django.db import models
 
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  password = models.CharField(max_length=255)

class Learn(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  number = models.CharField(max_length=255)
  courses = models.CharField(max_length=255)
  gender = models.CharField(max_length=255)

class Akshada(models.Model):
  aname = models.CharField(max_length=255)
  aemail = models.CharField(max_length=255)
  aissue = models.CharField(max_length=255)
  aremark = models.CharField(max_length=255)
  aservice = models.CharField(max_length=255)


class Fil(models.Model):
  file = models.FileField(upload_to="Media/")


class Mohan(models.Model):
  id = models.AutoField(primary_key=True)
  name = models.CharField(max_length=255)

