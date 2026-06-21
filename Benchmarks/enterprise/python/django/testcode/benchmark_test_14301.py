# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14301(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % (cookie_value,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
