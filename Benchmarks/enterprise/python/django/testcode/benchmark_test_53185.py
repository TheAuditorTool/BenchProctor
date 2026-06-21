# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53185(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
