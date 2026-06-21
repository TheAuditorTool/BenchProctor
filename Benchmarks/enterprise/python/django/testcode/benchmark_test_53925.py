# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import ast


def BenchmarkTest53925(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
