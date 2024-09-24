from django.db import models

# Create your models here.

class Project(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   goal = models.IntegerField() #use "Decimalfield" if need
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField(auto_now_add=True)

class Pledge(models.Model):
   amount = models.IntegerField()
   comment = models.CharField(max_length=200)
   anonymous = models.BooleanField()
   project = models.ForeignKey(
      'Project',
      on_delete=models.CASCADE,#means if delete the project, then all the pledges will be deleted
      related_name='pledges'#"the other end"
   )