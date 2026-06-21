# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


request_state: dict[str, str] = {}

def BenchmarkTest10818(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
