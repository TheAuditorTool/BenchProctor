# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import urllib.request


def BenchmarkTest65414(request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})
