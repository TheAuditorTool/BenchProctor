# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37462(request):
    cookie_value = request.COOKIES.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
