# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast


def BenchmarkTest17765(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
