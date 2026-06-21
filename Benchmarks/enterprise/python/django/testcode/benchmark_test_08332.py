# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08332(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
