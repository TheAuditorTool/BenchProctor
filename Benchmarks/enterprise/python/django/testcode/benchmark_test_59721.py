# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest59721(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
