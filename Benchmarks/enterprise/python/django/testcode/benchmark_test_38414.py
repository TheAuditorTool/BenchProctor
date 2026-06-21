# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38414(request):
    cookie_value = request.COOKIES.get('session_token', '')
    return JsonResponse({'error': str(cookie_value), 'stack': repr(locals())}, status=500)
