# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest36691(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
