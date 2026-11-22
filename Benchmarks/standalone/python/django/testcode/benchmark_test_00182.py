# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket
import urllib.parse


def BenchmarkTest00182(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    s = socket.create_connection((urllib.parse.urlparse(str(data)).hostname, 80))
    s.close()
    return JsonResponse({"saved": True})
