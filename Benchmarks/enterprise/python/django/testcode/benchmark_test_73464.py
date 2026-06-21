# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def normalise_input(value):
    return value.strip()

def BenchmarkTest73464(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = normalise_input(json_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return JsonResponse({"saved": True})
