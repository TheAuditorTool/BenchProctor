# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19346(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
