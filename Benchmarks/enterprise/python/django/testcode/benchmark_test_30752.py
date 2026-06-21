# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import defusedxml.ElementTree


request_state: dict[str, str] = {}

def BenchmarkTest30752(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
