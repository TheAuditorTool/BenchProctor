# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22031(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
