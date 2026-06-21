# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import defusedxml.ElementTree


def BenchmarkTest31100(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
