# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


request_state: dict[str, str] = {}

def BenchmarkTest29614(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    request_state['last_input'] = prop_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
