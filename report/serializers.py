from rest_framework import serializers

from .models import *



class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        read_only_fields = (
            'created_at',
        ),
        fields = [
            'id',
            'title',
            'name',
            'crime_location',
            'image',
            'created_at',
        ]