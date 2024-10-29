from rest_framework.decorators import api_view
from rest_framework.response import Response

from ativos.models import Computer
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


@api_view(["POST"])
def inventory(request):
    for key, value in filter(get_softwares, request.data["CONTENT"].items()):
        print(f"{key}: {value}")

    return Response(request.data)
