from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    content = models.TextField(max_length=5000)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)


    def __str__(self):
        return 'Message from ' + self.name 

class Email(models.Model):
    sno = models.AutoField(primary_key=True)
    email = models.CharField(max_length=25)

    def __str__(self):
        return self.email
    
    