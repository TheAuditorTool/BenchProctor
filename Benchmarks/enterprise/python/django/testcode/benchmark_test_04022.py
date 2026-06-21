# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest04022(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
