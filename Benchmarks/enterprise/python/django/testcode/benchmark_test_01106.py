# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os


def BenchmarkTest01106(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(dotenv_value)
    data = collected
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})
