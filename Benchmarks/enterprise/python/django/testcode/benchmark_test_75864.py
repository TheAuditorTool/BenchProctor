# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import json


def BenchmarkTest75864(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    requests.get(str(json_value))
    return JsonResponse({"saved": True})
