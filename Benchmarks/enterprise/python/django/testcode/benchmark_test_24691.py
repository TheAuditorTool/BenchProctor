# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest24691(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(origin_value)
    data = collected
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
