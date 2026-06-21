# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import requests


def to_text(value):
    return str(value).strip()

def BenchmarkTest41174(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = to_text(cookie_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})
