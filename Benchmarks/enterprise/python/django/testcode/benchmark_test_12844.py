# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest12844(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data), secure=True, httponly=True, samesite='Strict')
    return resp
