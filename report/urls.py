from .views import *
from django.urls import path

app_name = 'report'

urlpatterns = [
    path('createreport/', CreateReport.as_view(), name='createreport')

]