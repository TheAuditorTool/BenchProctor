# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest20842(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(forwarded_ip)
    data = collected
    processed = data[:64]
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
