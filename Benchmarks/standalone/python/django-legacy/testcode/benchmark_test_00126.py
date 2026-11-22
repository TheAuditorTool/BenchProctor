# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00126(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    parsed = json.loads(data)
    return JsonResponse({'parsed': str(parsed)}, status=200)
