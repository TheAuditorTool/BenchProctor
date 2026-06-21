# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15172(request):
    raw_body = request.body.decode('utf-8')
    data = raw_body if raw_body else 'default'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
