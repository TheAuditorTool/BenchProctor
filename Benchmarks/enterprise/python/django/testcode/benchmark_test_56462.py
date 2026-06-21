# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


request_state: dict[str, str] = {}

def BenchmarkTest56462(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})
