# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest06760(request):
    raw_body = request.body.decode('utf-8')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(raw_body))
    return resp
