# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07128(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    request.session.clear()
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
