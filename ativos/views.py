from datetime import datetime

from rest_framework.decorators import APIView, api_view
from rest_framework.response import Response
from rest_framework.views import Request

from ativos.models import Computer, Software
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
        data = request.data

        print(data["DEVICEID"])

        software_list = []

        # FIXME: lento demais
        # TODO: implementar transaction
        for software_data in data["CONTENT"]["SOFTWARES"]:
            software = Software(
                arch=software_data["ARCH"],
                name=software_data["NAME"],
                # install_date=datetime.strptime(software_data["INSTALLDATE"], "%d/%m/%Y"),
            )
            software_list.append(software)

        for software in software_list:
            software.save()

        computer = Computer(device_uid=data["DEVICEID"])
        computer.save()
        computer.softwares.set(software_list)

        return Response(status=200)
