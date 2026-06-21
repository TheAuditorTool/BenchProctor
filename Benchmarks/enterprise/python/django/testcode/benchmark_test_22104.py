# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest22104(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    if str(data).startswith('https://admin.internal/'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
