# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
import os


def relay_value(value):
    return value

def BenchmarkTest65374(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = relay_value(json_value)
    if os.environ.get("APP_ENV", "production") != "test":
        eval(str(data))
    return JsonResponse({"saved": True})
