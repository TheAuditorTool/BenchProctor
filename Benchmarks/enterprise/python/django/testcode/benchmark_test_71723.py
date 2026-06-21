# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest71723(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    size = min(int(json_value) if str(json_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
