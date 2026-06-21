# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75983(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
