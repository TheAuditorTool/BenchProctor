# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46438(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
