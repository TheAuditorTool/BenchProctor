# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest78161(request, path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    int(str(data))
    return JsonResponse({"saved": True})
