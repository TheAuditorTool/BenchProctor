# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest61986(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    return JsonResponse({"saved": True})
