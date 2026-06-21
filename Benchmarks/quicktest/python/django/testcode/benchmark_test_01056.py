# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01056(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    exec(str(processed))
    return JsonResponse({"saved": True})
