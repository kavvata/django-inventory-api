from rest_framework.decorators import api_view
from rest_framework.response import Response

from ativos.models import Computer
from ativos.serializer import ComputerSerializer


# Create your views here.
@api_view(['GET'])
def fetch(request):
    return Response(ComputerSerializer(Computer.objects.all(), many=True).data)