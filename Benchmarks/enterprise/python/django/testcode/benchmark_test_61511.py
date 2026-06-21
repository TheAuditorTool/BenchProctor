# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest61511(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = default_blank(json_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
