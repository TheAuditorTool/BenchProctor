# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import base64


def BenchmarkTest70362(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
