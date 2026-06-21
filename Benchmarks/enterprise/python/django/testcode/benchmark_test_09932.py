# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09932(request):
    multipart_value = request.POST.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return JsonResponse({"saved": True})
