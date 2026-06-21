# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest80308(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
