# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest00374(request):
    xml_value = request.body.decode('utf-8')
    data = '%s' % str(xml_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
