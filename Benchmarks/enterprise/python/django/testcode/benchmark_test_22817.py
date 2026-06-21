# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22817(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '{}'.format(cookie_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
