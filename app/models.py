from django.db import models

# Create your models here.
class Country(models.Model):
    c_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100)
   
    def __str__(self) -> str:
        return self.c_name
        

class Capital(models.Model):
    c_id=models.ForeignKey(Country,on_delete=models.CASCADE)
    cap_id=models.IntegerField(primary_key=True)
    c_name=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.c_name