# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest02121(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
