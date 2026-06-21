# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast


def BenchmarkTest58732(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    eval(compile('requests.get(str(data))', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
