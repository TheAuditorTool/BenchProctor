# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse


def ensure_str(value):
    return str(value)

def BenchmarkTest49083(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ensure_str(cookie_value)
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(target_url)})
