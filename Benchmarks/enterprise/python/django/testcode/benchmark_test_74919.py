# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74919(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
