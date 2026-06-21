# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest36880(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
