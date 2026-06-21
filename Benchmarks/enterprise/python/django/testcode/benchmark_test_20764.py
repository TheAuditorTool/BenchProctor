# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest20764(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    def normalize(value):
        return value.strip()
    data = normalize(json_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
