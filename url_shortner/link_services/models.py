from django.db import models

# Create your models here.

class Links (models.Model):
    input_link = models.TextField (blank=False)
    output_link = models.CharField (max_length= 30, unique=True, blank=False)
    user = models.ForeignKey (User,on_delete=models.CASCADE(),)


class Characteristic  (models.Model):

    lifespan = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    click_counts = models.IntegerField(default=0)








