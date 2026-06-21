# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest18342(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
