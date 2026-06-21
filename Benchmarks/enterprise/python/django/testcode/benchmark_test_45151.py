# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45151(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
