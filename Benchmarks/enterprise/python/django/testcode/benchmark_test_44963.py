# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44963(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
