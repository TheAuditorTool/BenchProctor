# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest00559(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parsed = json.loads(cookie_value)
    return JsonResponse({'parsed': str(parsed)}, status=200)
