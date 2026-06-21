# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import time
import ast


def BenchmarkTest55975(request):
    xml_value = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(xml_value))
    except (ValueError, SyntaxError):
        data = xml_value
    if time.time() > 1000000000:
        requests.get(str(data))
    return JsonResponse({"saved": True})
