# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import time
import ast


def BenchmarkTest54459(request, path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    if time.time() > 1000000000:
        eval(str(data))
    return JsonResponse({"saved": True})
