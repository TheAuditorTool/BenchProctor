# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest76565(request):
    multipart_value = request.POST.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    try:
        result = int(str(data))
    except Exception:
        pass
    return JsonResponse({"saved": True})
