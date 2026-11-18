# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest00436(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = (lambda v: v.strip())(referer_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
