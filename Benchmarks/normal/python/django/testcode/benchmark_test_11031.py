# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11031(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
