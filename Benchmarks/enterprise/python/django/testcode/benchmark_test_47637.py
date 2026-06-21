# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47637(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % (raw_body,)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
