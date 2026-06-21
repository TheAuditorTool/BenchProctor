# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest74226(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % (auth_header,)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
