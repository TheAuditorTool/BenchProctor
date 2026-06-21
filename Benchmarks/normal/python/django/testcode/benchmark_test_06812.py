# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import defusedxml.ElementTree


def BenchmarkTest06812(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
