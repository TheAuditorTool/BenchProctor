# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest06452(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = f'{json_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
