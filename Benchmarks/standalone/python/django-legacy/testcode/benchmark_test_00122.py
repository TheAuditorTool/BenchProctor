# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from dataclasses import dataclass
import socket
import urllib.parse


@dataclass
class FormData:
    payload: str
    content_type: str = 'text/plain'

def BenchmarkTest00122(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    form = FormData(payload=auth_header)
    data = form.payload
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
