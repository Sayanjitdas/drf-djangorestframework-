from django.shortcuts import render
from django.http import JsonResponse

def employeeView(request):

	emp ={
		'id': '123',
		'name': 'vicky',
		'salary':'12000'
	}

	return JsonResponse(emp)