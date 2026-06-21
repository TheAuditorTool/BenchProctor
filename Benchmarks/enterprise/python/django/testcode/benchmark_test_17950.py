# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets


def BenchmarkTest17950(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
