# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


request_state: dict[str, str] = {}

def BenchmarkTest74703(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
