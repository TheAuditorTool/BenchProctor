# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from pathlib import Path
import json


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02273(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
