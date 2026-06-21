# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import ast


def BenchmarkTest58640(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
