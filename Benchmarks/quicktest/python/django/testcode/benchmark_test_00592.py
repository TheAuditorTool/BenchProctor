# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def relay_value(value):
    return value

def BenchmarkTest00592(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
