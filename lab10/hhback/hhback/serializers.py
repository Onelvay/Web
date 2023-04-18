from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from .models import Company
from .models import Vacancy

class VacancySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    description = serializers.CharField()
    salary = serializers.FloatField()
    company = serializers.FloatField()

class CompanySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=40)
    description = serializers.CharField()
    city = serializers.CharField(max_length=20)
    address = serializers.CharField()

class CompanySerializer1(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'description', 'city','address']

class VacancySerializer1(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ['name','description','salary','company']

   
   

# class MyModelSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Company
#         fields = '__all__'
def encode():
    # company = Company("asdasd",'zxczxc','asdasdasd','qweqweqw')
    # companyc=CompanySerializer(company)
    # # model=Vacancy("abaay","asdfasd as d",234)
    # # model_c=VacancySerializer(model)
    # json=JSONRenderer().render(companyc.data)
    # print(json)
    # s= CompanySerializer1(instance=Company.objects.first())
    # print(s.data)

    companies=Company.objects.all()
    l=[]
    for company in companies:
        c=CompanySerializer1(instance=company)
        # json=JSONRenderer().render(c.data)
        l.append(c.data)
    print({'companies':l})
