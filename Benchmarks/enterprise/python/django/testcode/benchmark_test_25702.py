# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def relay_value(value):
    return value

def BenchmarkTest25702(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
