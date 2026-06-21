# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def ensure_str(value):
    return str(value)

def BenchmarkTest77097(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = ensure_str(json_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
