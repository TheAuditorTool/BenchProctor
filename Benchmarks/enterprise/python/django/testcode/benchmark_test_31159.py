# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def coalesce_blank(value):
    return value or ''

def BenchmarkTest31159(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = coalesce_blank(cookie_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
