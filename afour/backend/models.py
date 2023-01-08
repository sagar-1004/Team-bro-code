from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class skill(models.Model):
    username = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    skill_id = models.AutoField(primary_key=True)
    skill_name = models.CharField(max_length=10)
    skill_domain = models.CharField(max_length=10)
    skill_level = models.CharField(max_length=10)
    skill_exp = models.CharField(max_length=10)
    
