# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest60128(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    json.loads(json_value)
    return JsonResponse({"saved": True})
