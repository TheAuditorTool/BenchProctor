# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest00203(request):
    xml_value = request.body.decode('utf-8')
    data = str(xml_value).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
