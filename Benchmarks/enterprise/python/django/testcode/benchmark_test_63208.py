# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63208(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = []
    for token in str(cookie_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
