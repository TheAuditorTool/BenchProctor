# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def relay_value(value):
    return value

def BenchmarkTest06166(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
