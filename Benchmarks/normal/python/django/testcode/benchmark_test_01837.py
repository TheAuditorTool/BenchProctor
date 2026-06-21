# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest01837(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value}'
    allowed = {'config.json', 'index.html', 'readme.md'}
    if data not in allowed:
        return JsonResponse({'error': 'forbidden'}, status=403)
    checked_path = '/var/app/data/' + data
    os.unlink(checked_path)
    return JsonResponse({"saved": True})
