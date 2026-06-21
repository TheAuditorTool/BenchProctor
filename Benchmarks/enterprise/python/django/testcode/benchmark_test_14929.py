# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14929(request):
    cookie_value = request.COOKIES.get('session_token', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(cookie_value)})
