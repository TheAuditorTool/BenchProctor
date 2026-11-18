# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def BenchmarkTest00317(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
