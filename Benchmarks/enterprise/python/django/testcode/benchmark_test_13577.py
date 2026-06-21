# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13577(request):
    multipart_value = request.POST.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    processed = data[:64]
    request.session['data'] = str(processed)
    return JsonResponse({"saved": True})
