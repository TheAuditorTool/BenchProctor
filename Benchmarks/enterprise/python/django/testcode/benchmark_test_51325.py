# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51325(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
