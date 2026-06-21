# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest01130(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    json.loads(data)
    return JsonResponse({"saved": True})
