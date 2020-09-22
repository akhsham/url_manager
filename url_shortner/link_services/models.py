from django.db import models


# Create your models here.

class Links (models.Model):
    input_link = models.TextField(blank=False)
    input_text = models.TextField(default="TEXT", null=False, blank=False)
    expire_date = models.DateTimeField()
    life_span = models.DateTimeField()


    output_link = models.CharField(default= "text", max_length= 30, unique=True, blank=False)
    # output_link_90days = models.CharField(default= "text", max_length= 30, unique=True, blank=False)
    # output_link_premium = models.CharField(default= "text", max_length= 30, unique=True, blank=False)
#   user = models.ForeignKey (User,on_delete=models.CASCADE(),)


class Statistics  (models.Model):

    created_date = models.DateTimeField(auto_now_add=True)
    click_counts = models.IntegerField(default=0)








