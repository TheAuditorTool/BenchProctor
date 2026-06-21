# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import ast
import defusedxml.ElementTree


def BenchmarkTest09003(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = str(ast.literal_eval(env_value))
    except (ValueError, SyntaxError):
        data = env_value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
