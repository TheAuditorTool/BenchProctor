# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def ensure_str(value):
    return str(value)

def BenchmarkTest01137(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
