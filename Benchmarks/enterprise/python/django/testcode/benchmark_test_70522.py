# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest70522(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
