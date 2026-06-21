# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest21560(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': origin})
    return JsonResponse({"saved": True})
