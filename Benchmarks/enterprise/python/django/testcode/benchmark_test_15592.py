# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest15592(request):
    multipart_value = request.POST.get('multipart_field', '')
    request_state['last_input'] = multipart_value
    data = request_state['last_input']
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
