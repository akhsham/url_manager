from django.db import models

# Create your models here.

class Links (models.Model):
    input_link = models.TextField(blank=False)
    input_text = models.TextField(default="TEXT",null=False,blank=False)
    output_link_30days = models.CharField (default= "text", max_length= 30, unique=True, blank=False)
    output_link_90days = models.CharField (default= "text",max_length= 30, unique=True, blank=False)
    output_link_premium = models.CharField (default= "text",max_length= 30, unique=True, blank=False)

 #   user = models.ForeignKey (User,on_delete=models.CASCADE(),)


class Characteristic  (models.Model):

    lifespan = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    click_counts = models.IntegerField(default=0)








