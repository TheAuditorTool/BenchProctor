# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest75940(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
