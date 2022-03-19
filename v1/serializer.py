from rest_framework import serializers
from v1.models import ClassifyType, CompanyProfile, Log, ObjectData, Project, UserProfile, GroupProfile

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class GroupProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProfile
        fields = "__all__"

class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class ClassifyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassifyType
        fields = "__all__"

class CompanyProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyProfile
        fields = "__all__"

class ObjectDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObjectData
        fields = "__all__"