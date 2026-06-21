# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13186(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
