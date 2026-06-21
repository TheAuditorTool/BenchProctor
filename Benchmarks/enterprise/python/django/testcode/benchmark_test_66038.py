# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest66038(request):
    upload_name = request.FILES['upload'].name
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(upload_name)
    data = collected
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return JsonResponse({"saved": True})
