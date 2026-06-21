# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import urlparse
import json


request_state: dict[str, str] = {}

def BenchmarkTest02551(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    parsed = urlparse(data)
    if not (parsed.hostname or '').endswith(('.prod.internal', '.pycdn.io')):
        return JsonResponse({'error': 'forbidden host'}, status=403)
    target_url = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(target_url)})
