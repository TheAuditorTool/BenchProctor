# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02556(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    raise RuntimeError('processing failed: ' + str(data))
    return JsonResponse({"saved": True})
