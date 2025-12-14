from django.urls import path
from flats.views import flats_list, flat_details, flat_create

app_name = 'flats'

urlpatterns = [
    #http://localhost:8000/
    path('', flats_list, name='flats_list'),

    #http://localhost:8000/1/
    path('<int:flat_id>', flat_details, name='flat_details'),

    path('add/', flat_create, name="flat_create")
]

