# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest30737(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value:.200s}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
