# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest29667(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
