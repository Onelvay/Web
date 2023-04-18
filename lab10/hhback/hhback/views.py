from django.shortcuts import render
from .models import Company, Vacancy
from django.http import JsonResponse
from .serializers import CompanySerializer1
from .serializers import VacancySerializer1
from rest_framework.renderers import JSONRenderer
import json

def Companies(request):
    companies=Company.objects.all()
    l=[]
    for company in companies:
        c=CompanySerializer1(instance=company)
        l.append(c.data)
    return json.dumps(l)

def getCompany(request, id):
    company = CompanySerializer1(instance=Company.objects.get(id = id))
    return JsonResponse(company.data)

def Vacancies(request):
    vacancy=Vacancy.objects.all()
    l=[]
    for v in vacancy:
        c=VacancySerializer1(instance=v)
        l.append(c.data)
    return JsonResponse({'vacancies':l},status=200)

def getVacancy(request, id):
    vacancy=VacancySerializer1(instance=Vacancy.objects.get(id = id))
    return JsonResponse(vacancy.data, status=200)

def topTenSalaries(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    l=[]
    for v in vacancies:
        c=VacancySerializer1(instance=v)
        l.append(c.data)
    return JsonResponse({'vacancies':l},status=200)


def getVacancyByCompany(request, id):
    vacancies = Vacancy.objects.filter(company_id=id)
    l=[]
    for v in vacancies:
        c=VacancySerializer1(instance=v)
        l.append(c.data)
    return JsonResponse({'vacancies':l},status=200)
