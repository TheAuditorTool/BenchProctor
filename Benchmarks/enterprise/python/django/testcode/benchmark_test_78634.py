# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
from django.http import HttpResponse
import json
import os


request_state: dict[str, str] = {}

def BenchmarkTest78634(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    request_state['last_input'] = json_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)
