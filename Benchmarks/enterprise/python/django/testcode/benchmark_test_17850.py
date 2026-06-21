# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17850(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
