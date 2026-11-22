# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
import urllib.parse


def BenchmarkTest00050(request):
    xml_value = request.body.decode('utf-8')
    data = (lambda v: v.strip())(xml_value)
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
