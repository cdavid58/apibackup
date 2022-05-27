from django.conf.urls import url
from .views import *

urlpatterns=[
		url(r'^Create_BackUp_Payroll$',Create_BackUp_Payroll,name="Create_BackUp_Payroll"),
		url(r'^Create_BackUp_PDF$',Create_BackUp_PDF,name="Create_BackUp_PDF"),
	]