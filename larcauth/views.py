from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime

# Create your views here.
@api_view(['GET'])
def index(request):
    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    message = 'LarcServer is alive ! Its Current time is --> '
    return Response (data=message + date, status = status.HTTP_200_OK)
