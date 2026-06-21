# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


request_state: dict[str, str] = {}

def BenchmarkTest01305(request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    request_state['last_input'] = config_value
    data = request_state['last_input']
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
