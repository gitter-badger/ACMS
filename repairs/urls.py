#from .models import Products, Service_Centres
from django.urls import include, path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('<int:product_id>/',views.centres,name='centres'),
	]

