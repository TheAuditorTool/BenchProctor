# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27601(request):
    cookie_value = request.COOKIES.get('session_token', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(cookie_value))
    return resp
