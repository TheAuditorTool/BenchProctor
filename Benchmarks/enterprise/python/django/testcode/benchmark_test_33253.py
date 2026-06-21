# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest33253(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(json_value)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
