# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest79903(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
