from django.urls import path
from flats.views import flats_list

app_name = 'flats'

urlpatterns = [
    #http://localhost:8000/
    path('', flats_list, name='flats_list')
]