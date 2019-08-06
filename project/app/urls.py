from django.urls import path
from .views import *

urlpatterns = [
		path('', Home, name= ' home'),	
		path('input_/', make_pridiction, name='pridict'),
		path('input/data/', pridict,name="pridict"),
]