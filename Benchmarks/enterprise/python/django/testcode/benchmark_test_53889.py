# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest53889(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
