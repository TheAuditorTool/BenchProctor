# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import socket


def relay_value(value):
    return value

def BenchmarkTest40294(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    eval(compile('s = socket.create_connection((str(data), 80))\ns.close()', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
