# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from urllib.parse import unquote


def BenchmarkTest78658(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    arr = [10, 20, 30, 40, 50]
    idx = int(str(processed))
    return JsonResponse({'lookup': arr[idx]}, status=200)
