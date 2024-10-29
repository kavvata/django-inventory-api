from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.views import Request

from ativos.models import Computer
from ativos.parsers import XMLParser
from ativos.serializer import ComputerSerializer


def get_softwares(pair):
    key, value = pair

    if key != "SOFTWARES":
        return False

    return True


# Create your views here.
@api_view(["GET"])
def fetch(request):
    return Response(ComputerSerializer(Computer.objects.all(), many=True).data)


class InventoryView(APIView):
    parser_classes = [XMLParser]

    def post(self, request: Request):
        return Response(request.data)
