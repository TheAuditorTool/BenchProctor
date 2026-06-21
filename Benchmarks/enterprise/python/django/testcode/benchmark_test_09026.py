# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import pickle


def BenchmarkTest09026(request):
    xml_value = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
