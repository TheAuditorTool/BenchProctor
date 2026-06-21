# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24256(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
