# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest50447(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    int(str(json_value))
    return JsonResponse({"saved": True})
