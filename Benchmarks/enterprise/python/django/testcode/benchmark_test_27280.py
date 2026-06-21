# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest27280(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = '%s' % str(json_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
