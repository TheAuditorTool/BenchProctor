# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import time
import ast
import subprocess


def BenchmarkTest80149(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if time.time() > 1000000000:
        subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
