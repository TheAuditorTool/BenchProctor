# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import json


request_state: dict[str, str] = {}

def BenchmarkTest04528(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
