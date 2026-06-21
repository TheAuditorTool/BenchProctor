# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess
import ast


def BenchmarkTest26439(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
