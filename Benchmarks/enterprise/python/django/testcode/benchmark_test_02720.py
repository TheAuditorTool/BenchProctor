# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02720(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
