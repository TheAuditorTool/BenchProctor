# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75273(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data, _sep, _rest = str(cookie_value).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
