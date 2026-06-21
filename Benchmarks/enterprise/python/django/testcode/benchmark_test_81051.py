# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest81051(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
