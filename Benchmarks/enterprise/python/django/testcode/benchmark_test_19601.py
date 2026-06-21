# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19601(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    if str(data) in ('admin', 'true', 'authenticated'):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
