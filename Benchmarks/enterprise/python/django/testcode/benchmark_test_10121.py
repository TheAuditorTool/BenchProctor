# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10121(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
