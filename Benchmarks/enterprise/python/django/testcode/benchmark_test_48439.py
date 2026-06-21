# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest48439(request):
    cookie_value = request.COOKIES.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
