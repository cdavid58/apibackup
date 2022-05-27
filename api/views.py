from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import render
from base64 import b64decode
from .models import *
import base64


@api_view(['POST'])
def Create_BackUp_Payroll(request):
	data = request.data
	message = ""
	try:
		bp = BackUp_Payroll.objects.get(payroll_document = data['payroll'])
	except BackUp_Payroll.DoesNotExist:
		bp = None
	if bp is None:
		BackUp_Payroll(
			company = data['company'],
			payroll_document = data['payroll'],
			month = data['month'],
			anio = data['anio']
		).save()
		message = 'Success'
	else:
		message = "Esa nomina ya esta guardada en el sistema"

	return Response({'Message':message})

@api_view(['POST'])
def Create_BackUp_PDF(request):
	data = request.data
	try:
		BackUp_PDFS(
			company = data['company'],
			pdf = data['pdf'],
			type_pdf = data['type_pdf'],
			number = data['number'],
			prefix = data['prefix'],
			token = data['token'],
			pk_company = data['pk_company'],
			pk_invoice = data['pk_invoice']
		).save()
	except Exception as e:
		message = "Error"	

	encoded = data['pdf'].encode('ascii')
	pdf = BackUp_PDFS.objects.get(number = data['number'],type_pdf = data['type_pdf'],company = data['company'])
	pdf.Send_Email()
	message = "Success"
	return Response({'Message':message})

