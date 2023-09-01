from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer
from .models import Customer

# Create your views here.

class CustomerAPI(ModelViewSet):
    """
    Using ModelViewSet instead of generic views because we just need to enter customer informations and retrieve them.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

