# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


request_state: dict[str, str] = {}

def BenchmarkTest50422(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
