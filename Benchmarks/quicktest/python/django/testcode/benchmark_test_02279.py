# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest02279(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
