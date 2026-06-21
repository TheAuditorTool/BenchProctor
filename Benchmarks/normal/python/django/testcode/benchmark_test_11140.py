# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


request_state: dict[str, str] = {}

def BenchmarkTest11140(request):
    xml_value = request.body.decode('utf-8')
    request_state['last_input'] = xml_value
    data = request_state['last_input']
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
