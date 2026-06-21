# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest63806(request):
    cookie_value = request.COOKIES.get('session_token', '')
    def normalize(value):
        return value.strip()
    data = normalize(cookie_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
