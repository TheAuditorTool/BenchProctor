# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
from urllib.parse import unquote


def BenchmarkTest41091(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
