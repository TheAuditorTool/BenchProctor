# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51765(request):
    user_id = request.GET.get('id', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(user_id)
    data = collected
    processed = data[:64]
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
