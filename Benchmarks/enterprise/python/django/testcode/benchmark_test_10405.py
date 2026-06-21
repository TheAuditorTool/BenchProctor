# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest10405(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    if not str(json_value).isdigit():
        raise ValueError('invalid input: ' + str(json_value))
    return JsonResponse({"saved": True})
