# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74729(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
