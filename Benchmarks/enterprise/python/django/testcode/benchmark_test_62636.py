# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex
import ast


def BenchmarkTest62636(request, path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
