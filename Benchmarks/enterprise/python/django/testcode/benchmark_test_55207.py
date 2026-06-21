# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def coalesce_blank(value):
    return value or ''

def BenchmarkTest55207(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = coalesce_blank(cookie_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
