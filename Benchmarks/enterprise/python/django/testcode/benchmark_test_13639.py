# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


def BenchmarkTest13639(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', cookie_value):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = cookie_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(processed)})
