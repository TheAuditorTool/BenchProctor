# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
from app_runtime import auth_check


def BenchmarkTest68733(request):
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    try:
        data = str(ast.literal_eval(file_value))
    except (ValueError, SyntaxError):
        data = file_value
    auth_check('user', data)
    return JsonResponse({"saved": True})
