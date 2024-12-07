from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Project, Pledge


@receiver(post_save, sender=Pledge)
@receiver(post_delete, sender=Pledge)
def update_project_funding(sender, instance, **_kwargs):
    project = instance.project
    project.current_funded_amount = sum(
        pledge.amount for pledge in project.pledges.all()
    )
    
    project.save()