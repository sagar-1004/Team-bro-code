from django.shortcuts import render
from rest_framework import status, viewsets
import requests
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework import serializers
from django.core.files.storage import FileSystemStorage
from django.core.files.base import ContentFile
from django.shortcuts import render, HttpResponse, redirect
import csv
from .models import *
from .serializer import *

# Create your views here.


class Skillview(APIView):

    def get(self, request, pk=None):
        id = pk
        if id is not None:
            queryset = skill.objects.filter(username=id)
            serializer1_class = skillSerializer(queryset, many=True)
            # print(queryset)
            return Response(serializer1_class.data)
        queryset = skill.objects.all()
        serializer_class = skillSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def put(self, request, pk):
        id = pk
        queryset = skill.objects.get(skill_id=id)
        serializer_class = skillSerializer(queryset, data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg': serializer_class.data})
        return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete (self,request,pk):
        id=pk
        member = skill.objects.get(skill_id=pk)
        member.delete()
        return Response({'msg':'Deleted'})

    def post(self,request):
        serializer_class=skillSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return redirect('/viewskill')
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)    

    def patch(self, request, pk):
        id = pk
        queryset = skill.objects.get(skill_id=id)
        serializer_class = skillSerializer(
            queryset, data=request.data, partial=True)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response({'msg': 'Partial Data Updated', 'data': serializer_class.data})
        return Response(serializer_class.errors)


def team_csv(request):
    domain = request.GET.get('skill_domain', '')
    name = request.GET.get('skill_name', '')
    level = request.GET.get('skill_level', '')
    experience = request.GET.get('skill_experience', '')

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=team_list.csv'

    # Create a csv writer
    writer = csv.writer(response)

    if level == 'basic':
        data = skill.objects.filter(
            skill_domain=domain, skill_name=name, skill_exp__gte=experience).distinct()
    elif level == 'inter':
        data = skill.objects.filter(
            skill_domain=domain, skill_name=name, skill_exp__gte=experience).exclude(skill_level='basic')
    else:
        data = skill.objects.filter(
            skill_domain=domain, skill_name=name, skill_level='exp', skill_exp__gte=experience)

    # Designate The Model
    
    # lab_els = skill.objects.filter(test_type_id=test_typ.test_type_id)

    # c = ['Team members']
    # writer.writerow(c)

    # p=[]

    # for elts in data:

    #     p.append(elts.username)
    #     writer.writerows(p)

    # # Add column headings to the csv file
    
    # return response
    # data = list(data.values())
    header = ['Name']
    print(data)
    c = []
    l = 0

    for elts in data:
        l=l+1

    for i in range(l):

        # Append an empty sublist inside the list
            c.append([])

            for elts in data:
                string = str(elts.username)
                c[i].append(string)




    # Add column headings to the csv file
    writer.writerow(header)
    writer.writerow(c)
    return response


fs = FileSystemStorage(location='tmp/')