# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest01869(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
