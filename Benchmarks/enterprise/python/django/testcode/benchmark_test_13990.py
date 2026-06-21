# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13990(request):
    raw_body = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    processed = data[:64]
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
