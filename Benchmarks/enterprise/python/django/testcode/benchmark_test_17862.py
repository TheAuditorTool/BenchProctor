# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17862(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(ua_value)
    data = collected
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
