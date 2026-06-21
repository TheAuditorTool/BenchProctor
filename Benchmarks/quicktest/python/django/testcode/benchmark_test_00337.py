# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import socket


def BenchmarkTest00337(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
