# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def to_text(value):
    return str(value).strip()

def BenchmarkTest28814(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = to_text(json_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})
