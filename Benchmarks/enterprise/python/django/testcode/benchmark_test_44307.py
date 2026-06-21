# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import os


request_state: dict[str, str] = {}

def BenchmarkTest44307(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return JsonResponse({"saved": True})
