# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest34757(request):
    cookie_value = request.COOKIES.get('session_token', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(cookie_value), max_age=86400)
    return resp
