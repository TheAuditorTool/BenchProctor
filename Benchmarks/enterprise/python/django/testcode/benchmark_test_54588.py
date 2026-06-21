# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54588(request):
    raw_body = request.body.decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
