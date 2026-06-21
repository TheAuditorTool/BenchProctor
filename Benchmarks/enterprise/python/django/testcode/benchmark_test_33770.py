# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import ast


def BenchmarkTest33770(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
