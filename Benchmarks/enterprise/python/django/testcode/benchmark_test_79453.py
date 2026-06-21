# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest79453(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})
