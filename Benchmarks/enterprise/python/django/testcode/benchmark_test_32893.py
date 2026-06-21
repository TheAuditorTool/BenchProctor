# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32893(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
