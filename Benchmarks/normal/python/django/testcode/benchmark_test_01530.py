# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01530(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
