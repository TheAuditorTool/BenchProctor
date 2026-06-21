# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest37797(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    raise RuntimeError('processing failed: ' + str(json_value))
    return JsonResponse({"saved": True})
