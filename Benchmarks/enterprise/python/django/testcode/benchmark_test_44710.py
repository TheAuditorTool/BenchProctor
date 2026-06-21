# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest44710(request):
    xml_value = request.body.decode('utf-8')
    if xml_value:
        data = xml_value
    else:
        data = ''
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
