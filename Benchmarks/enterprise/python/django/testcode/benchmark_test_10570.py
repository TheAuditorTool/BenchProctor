# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest10570(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    allowed = {'config.json', 'index.html', 'readme.md'}
    if json_value not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + json_value
    with open(checked_path, 'wb') as fh:
        fh.write(b'data')
    return JsonResponse({"saved": True})
