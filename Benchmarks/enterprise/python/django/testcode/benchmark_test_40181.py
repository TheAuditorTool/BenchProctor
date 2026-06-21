# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest40181(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    if str(data) == 'S3cr3tToken':
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
