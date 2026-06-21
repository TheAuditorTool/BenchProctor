# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest65460(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
