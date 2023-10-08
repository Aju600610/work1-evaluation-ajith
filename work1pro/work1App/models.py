from django.db import models

# Create your models here.
class Dictionary(models.Model):
    label = models.CharField(max_length=100) 
    description = models.CharField(max_length=200)   
    search_count = models.IntegerField()    
    
    
    
    def __str__(self) :
        return self.name
    

    
