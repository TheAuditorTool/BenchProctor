# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52847(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    int(str(data))
    return JsonResponse({"saved": True})
