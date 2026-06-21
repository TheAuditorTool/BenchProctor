# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest12482(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    s = socket.create_connection((str(forwarded_ip), 80))
    s.close()
    return JsonResponse({"saved": True})
