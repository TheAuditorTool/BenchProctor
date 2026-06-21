# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest38178(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = (lambda v: v.strip())(json_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
