from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum
#from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.conf import settings

# Create your models here.


class Project(models.Model):
   title = models.CharField(max_length=200)
   description = models.TextField()
   goal = models.IntegerField() #use "Decimalfield" if need
   image = models.URLField()
   is_open = models.BooleanField()
   date_created = models.DateTimeField(auto_now_add=True)
   current_funded_amount = models.IntegerField()
   owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      related_name='owned_projects'
   )

   def calculate_funding_progress(self):
      pledges = self.pledges.aggregate(total_pledged=Sum('amount'))['total_pledged'] or 0
      self.current_funded_amount = pledges
      return (self.current_funded_amount / self.goal) * 100 if self.goal > 0 else 0

class Pledge(models.Model):
   amount = models.IntegerField()
   comment = models.CharField(max_length=200)
   anonymous = models.BooleanField()
   project = models.ForeignKey(
      'Project',
      on_delete=models.CASCADE,#means if delete the project, then all the pledges will be deleted
      related_name='pledges'#"the other end"
   )
   supporter = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE,
      related_name='pledges'
   )

   def save(self, *args, **kwargs):
    super().save(*args, **kwargs)

    if self.project:  # Ensure project exists
         try:
            self.project.calculate_funding_progress()
            self.project.save()
         except Exception as e:
                print("Error updating funding progress:", str(e))
                raise e 