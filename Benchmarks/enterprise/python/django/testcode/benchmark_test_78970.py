# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest78970(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
