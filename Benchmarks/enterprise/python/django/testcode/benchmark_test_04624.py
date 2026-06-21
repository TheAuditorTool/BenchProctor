# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def relay_value(value):
    return value

def BenchmarkTest04624(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
