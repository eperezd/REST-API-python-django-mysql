from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Company
import json

# Create your views here.
class CompanyView(View):
    @method_decorator(csrf_exempt) #decorador de metodos
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            companies=list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company=companies[0]
                datos = {'mensaje': "Success", 'companies': company}
            else:
                datos = {'mensaje': "Success not found"}
            return JsonResponse(datos)    
        else:        
            companies = list(Company.objects.values())
            if len(companies)> 0:
                datos = {'mensaje': "Success", 'companies': companies}
            else:
                datos = {'mensaje': "Error"}
            return JsonResponse(datos)

    def post(self, request, *args, **kwargs):
        #print(request.body)
        jd =json.loads(request.body)
        #print(jd)
        Company.objects.create(name=jd['name'], webwsite=jd['website'], foundation=jd['foundation']  )
        datos = {'mensaje': "Success"}
        return JsonResponse(datos)

    
    def put(self, request, id):
        jd = json.loads(request.body)
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.webwsite = jd['website']
            company.foundation = jd['foundation']
            company.save()  
            datos = {'mensaje': "Success"}
        else:
            datos = {'mensaje': "Company not found"}
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos = {'mensaje': "Success"}
        else:
            datos = {'mensaje': "Company not found"}
        return JsonResponse(datos)

    def create(self, request):
        pass
    def update(self, request, *args, **kwargs):
        pass

