# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast


def BenchmarkTest13522(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    eval(compile("os.system('echo ' + str(data))", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
