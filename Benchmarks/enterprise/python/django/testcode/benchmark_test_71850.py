# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import ast


def BenchmarkTest71850(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
