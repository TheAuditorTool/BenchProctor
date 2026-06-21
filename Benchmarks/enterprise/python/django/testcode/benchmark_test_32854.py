# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import importlib


def BenchmarkTest32854(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
