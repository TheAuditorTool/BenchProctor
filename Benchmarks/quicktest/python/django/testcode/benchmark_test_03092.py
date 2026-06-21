# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import ast


def BenchmarkTest03092(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
