# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import ast


def BenchmarkTest21195(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
