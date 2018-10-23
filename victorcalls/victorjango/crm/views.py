from django.shortcuts import render
import flask_excel as excel
from werkzeug.utils import secure_filename
from flask import Flask, request
import pyexcel
import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework import status
import psycopg2
import json
from psycopg2.extras import RealDictCursor
con = psycopg2.connect(dbname='leadpoliceb', user='postgres', host='localhost', password='Bismillah@123')
from django.http import HttpResponseRedirect
from django.shortcuts import render
#from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
#from somewhere import handle_uploaded_file

def open():
    global con
    #cur = con.cursor()
    con = psycopg2.connect(dbname='leadpoliceb', user='postgres', host='localhost', password='Bismillah@123')
    cur = con.cursor(cursor_factory=RealDictCursor)
    return cur


def close(cur):
    global con
    con.commit()
    cur.close()
    con.close()
    return True


class DocumentsList(APIView):
    def get(self,request):
        records = Documents.objects.all()
        serializer = DocumentsSerializer(records,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DocumentsSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Documents_of_project_List(APIView):
    def get(self,request, project_id):
        records = Documents.objects.filter(projectid= project_id)
        serializer = DocumentsSerializer(records,many=True)
        return Response(serializer.data)


class Document_with_projectid_documentid(APIView):
    def get(self,request, project_id,document_id):
        records = Documents.objects.filter(projectid= project_id,id=document_id)
        serializer = DocumentsSerializer(records,many=True)
        return Response(serializer.data)


class CompanyList(APIView):
    def get(self,request):
        records = Company.objects.all()
        serializer = CompanySerializer(records,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Company_company_id_get_update_delete(APIView):
    def get(self,request,company_id, Format=None):
        records = Company.objects.get(pk=company_id)
        serializer = CompanySerializer(records)
        return Response(serializer.data)

    def put(self,request,company_id, Format=None):
        records = Company.objects.get(pk=company_id)
        serializer = CompanySerializer(records,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_id, format=None):
        user = Company.objects.get(pk=company_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AspnetusersList(APIView):
    def get(self,request):
        documents = Aspnetusers.objects.all()
        serializer = AspnetusersSerializer(documents,many=True)
        return Response(serializer.data)


    def post(self, request):
        serializer = AspnetusersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Aspnetusers_get_update_delete(APIView):
    """
    update or delete a user instance.
    """

    def get(self, request, user_id, format=None):
        user = Aspnetusers.objects.get(pk=user_id)
        serializer = AspnetusersSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        user = Aspnetusers.objects.get(pk=user_id)
        serializer = AspnetusersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        user = Aspnetusers.objects.get(pk=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Aspnetusers_of_companyList(APIView):
    def get(self,request,company_id):
        documents = Aspnetusers.objects.filter(companyid=company_id)
        serializer = AspnetusersSerializer(documents,many=True)
        return  Response(serializer.data)


class Aspnetusers_of_username(APIView):
    def get(self,request,user_name):
        documents = Aspnetusers.objects.filter(username=user_name)
        serializer = AspnetusersSerializer(documents,many=True)
        return Response(serializer.data)


class AspnetrolesList(APIView):
    def get(self,request):
        documents = Aspnetroles.objects.all()
        serializer = AspnetrolesSerializer(documents,many=True)
        return Response(serializer.data)

    def post(self, request, Format=None):
        serializer = AspnetrolesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectList(APIView):
    def get(self,request):
        records = Project.objects.all()
        serializer = ProjectSerializer(records,many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Project_project_id_get_update_delete(APIView):
    def get(self,request,project_id,Format=None):
        records = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(records)
        return Response(serializer.data)

    def put(self,request,project_id, Format=None):
        record = Project.objects.get(pk=project_id)
        serializer = ProjectSerializer(record,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, project_id, format=None):
        record = Project.objects.get(pk=project_id)
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Projects_of_company(APIView):
    def get(self,request,company_id):
        records = Project.objects.filter(companyid=company_id)
        serializer = ProjectSerializer(records,many=True)
        return  Response(serializer.data)

class UsersJoinList(APIView):
    def get(self,request):
        cursor = open()
        query = "SELECT documents.projectid FROM documents INNER JOIN project on documents.projectid = project.projectid"
        cursor.execute(query)
        records = cursor.fetchall()
        r = json.dumps(records)
        loaded_r = json.loads(r)
        return Response(loaded_r)


class Aspnetusers_join_aspnetroles(APIView):
    def get(self,request, user_name):
        cursor = open()
        join_query = "select r.name, U.* from (select * from aspnetusers where companyid in " \
                "(select companyid from aspnetusers where username=" + "'" + user_name + "'" + "limit 1)) as U " \
                "join aspnetroles r on CAST(U.roleid AS INTEGER)=r.id;"
        cursor.execute(join_query)
        records = cursor.fetchall()
        dump_records = json.dumps(records,sort_keys=True, default=str)
        loaded_records = json.loads(dump_records)
        return Response(loaded_records)


class LeadsList(APIView):
    def get(self,request):
        documents = Leads.objects.all()
        serializer = LeadsSerializer(documents,many=True)
        return  Response(serializer.data)

    def post(self, request, format=None):
        serializer = LeadsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class UploadFiles(APIView):
    def post(self,request):
        f = request.FILES['file']
        print(f.name)
        myfile = pd.read_excel(f)
        #print(myfile.to_json(orient='records'))
        serializer = LeadsSerializer(data=myfile.to_json(orient='records'))
        if serializer.is_valid():
            serializer.save()
        #print(myfile.head())
        return Response('success')
# Create your views here.
from django.shortcuts import render

# Create your views here.
