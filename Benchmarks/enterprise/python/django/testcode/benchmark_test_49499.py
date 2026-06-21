# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest49499(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
