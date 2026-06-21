# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def relay_value(value):
    return value

def BenchmarkTest09910(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
