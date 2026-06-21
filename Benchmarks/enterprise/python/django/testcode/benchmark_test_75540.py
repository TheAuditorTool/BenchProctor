# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import json


request_state: dict[str, str] = {}

def BenchmarkTest75540(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
