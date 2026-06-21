# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest81309(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
