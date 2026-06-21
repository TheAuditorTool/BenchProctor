# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72924(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
