# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import defusedxml.ElementTree


def BenchmarkTest03150(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
