# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json
import time


request_state: dict[str, str] = {}

def BenchmarkTest01728(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return JsonResponse({"saved": True})
