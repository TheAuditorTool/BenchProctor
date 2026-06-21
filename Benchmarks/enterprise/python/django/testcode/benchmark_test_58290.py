# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58290(request):
    cookie_value = request.COOKIES.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
