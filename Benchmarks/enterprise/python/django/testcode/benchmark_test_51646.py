# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import re
import json


request_state: dict[str, str] = {}

def BenchmarkTest51646(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
