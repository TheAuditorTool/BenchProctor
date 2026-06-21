# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest04266(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = '%s' % str(cookie_value)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
