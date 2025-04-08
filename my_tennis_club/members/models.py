from django.db import models

class Member(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
    phone=models.CharField(null=True,blank=True)
    joined_date=models.DateField(null=True)
    slug=models.SlugField(default="",null=False)

    def __str__(self):
        return f"{self.lastname}{self.firstname}"