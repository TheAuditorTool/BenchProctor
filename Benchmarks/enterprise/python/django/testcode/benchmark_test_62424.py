# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest62424(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = unquote(cookie_value)
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
