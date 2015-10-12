from django.db import models
from django.contrib.auth.models import User

class Donut(models.Model):
    donut_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date given')
    user = models.ForeignKey(User)
