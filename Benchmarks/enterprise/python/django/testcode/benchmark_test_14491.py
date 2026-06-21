# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14491(request):
    raw_body = request.body.decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
