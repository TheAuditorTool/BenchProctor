# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import socket


def BenchmarkTest24568(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
