# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33130(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
