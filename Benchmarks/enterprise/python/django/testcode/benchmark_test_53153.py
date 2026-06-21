# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53153(request):
    raw_body = request.body.decode('utf-8')
    data, _sep, _rest = str(raw_body).partition('\x00')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
