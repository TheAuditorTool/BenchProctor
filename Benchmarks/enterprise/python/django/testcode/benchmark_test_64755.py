# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest64755(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    if os.environ.get("APP_ENV", "production") != "test":
        with open('/var/www/html/exports/report.txt', 'w') as fh:
            fh.write(str(data))
    return JsonResponse({"saved": True})
