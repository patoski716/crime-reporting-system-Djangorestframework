from django.shortcuts import render

# Create your views here.
from .models import Report
from .serializers import ReportSerializer
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser



# class CreateReport(generics.ListCreateAPIView):
#     parser_classes = [ MultiPartParser, FormPaser]
#     queryset = Report.objects.all()
#     serializer_class = ReportSerializer

class CreateReport(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer_class = ReportSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer_class.errors, status=status.HTTP_400_BAD_REQUEST)