# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast


def BenchmarkTest68204(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})
