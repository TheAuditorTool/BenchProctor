# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


request_state: dict[str, str] = {}

def BenchmarkTest34224(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    def _primary():
        requests.get(str(data))
    _handlers = {"primary": _primary}
    _handlers["primary"]()
    return JsonResponse({"saved": True})
