# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46919(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
