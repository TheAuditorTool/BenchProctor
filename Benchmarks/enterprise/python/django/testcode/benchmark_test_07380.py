# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest07380(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = str(auth_header).replace('\x00', '')
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
