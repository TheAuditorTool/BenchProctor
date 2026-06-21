# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest36296(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = json_value if json_value else 'default'
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
