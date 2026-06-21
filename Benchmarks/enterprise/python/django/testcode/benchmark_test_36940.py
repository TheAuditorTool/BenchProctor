# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time


request_state: dict[str, str] = {}

def BenchmarkTest36940(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if time.time() > 1000000000:
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return JsonResponse({"saved": True})
