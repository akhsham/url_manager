#from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Links
from django.urls import reverse_lazy


class CreateUrl(CreateView):
    model = Links
    fields = ["input_link", "life_span", "output_link"]
    success_url = reverse_lazy("thanks")




