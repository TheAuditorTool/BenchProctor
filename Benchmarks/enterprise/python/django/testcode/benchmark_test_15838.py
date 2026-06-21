# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import json


def BenchmarkTest15838(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = json.loads(host_value).get('value', host_value)
    except (json.JSONDecodeError, AttributeError):
        data = host_value
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
