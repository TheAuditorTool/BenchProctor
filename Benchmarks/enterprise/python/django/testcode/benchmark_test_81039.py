# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest81039(request):
    cookie_value = request.COOKIES.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
