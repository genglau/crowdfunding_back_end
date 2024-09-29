

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    def __str__(self) -> str:
        return f"Retriving username: {self.username}, Last Login: {self.last_login}"
