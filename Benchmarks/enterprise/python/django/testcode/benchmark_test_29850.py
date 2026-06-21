# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def normalise_input(value):
    return value.strip()

def BenchmarkTest29850(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = normalise_input(cookie_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
