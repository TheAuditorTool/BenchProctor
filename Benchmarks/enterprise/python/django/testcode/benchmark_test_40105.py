# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest40105(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
