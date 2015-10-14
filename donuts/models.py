from django.db import models

class Chat(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    def __str__(self):
        return (self.first_name + ' ' + self.last_name)

class Donut(models.Model):
    donut_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date given')
    chat = models.ForeignKey(Chat)
    def __str__(self):
        return (self.chat.first_name+' - '+self.donut_text)
