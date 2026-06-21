# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import defusedxml.ElementTree


def BenchmarkTest21771(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
