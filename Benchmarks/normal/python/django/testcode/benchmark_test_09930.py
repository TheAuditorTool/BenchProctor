# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast


def BenchmarkTest09930(request, path_param):
    path_value = path_param
    try:
        data = str(ast.literal_eval(path_value))
    except (ValueError, SyntaxError):
        data = path_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
