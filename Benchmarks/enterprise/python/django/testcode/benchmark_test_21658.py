# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest21658(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
