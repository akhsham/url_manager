# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('', views.post_list, name='post_list'),
# ]

from django.urls import path
from .views import CreateUrl

urlpatterns = [
    path('', CreateUrl.as_view(), name="HOME"),
]