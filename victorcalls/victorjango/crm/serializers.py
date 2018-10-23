from rest_framework import serializers
from .models import Documents, Company, Aspnetusers, Leads, Project, Integrations,\
    Leaditems, Aspnetroles, Location, Attendance, Refreshtokens, Companytype

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Documents
        fields = '__all__'
        #fields = ('name',)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanytypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companytype
        fields = '__all__'

class AspnetusersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspnetusers
        fields = '__all__'
        # fields = [
        #     'id',
        #     'username',
        #     'user_id',
        #     'password',
        #     'cid'
        # ]


class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leads
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class IntegrationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integrations
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class LeaditemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leaditems
        fields = '__all__'

class AspnetrolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aspnetroles
        fields = '__all__'