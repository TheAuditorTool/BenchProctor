# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest10844(request):
    raw_body = request.body.decode('utf-8')
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(raw_body), secure=True, httponly=True, samesite='Strict')
    return resp
