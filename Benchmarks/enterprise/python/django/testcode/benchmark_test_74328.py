# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest74328(request):
    cookie_value = request.COOKIES.get('session_token', '')
    if cookie_value:
        data = cookie_value
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
