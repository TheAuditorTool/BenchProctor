# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import requests


def BenchmarkTest11500(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    processed = data[:64]
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return JsonResponse({"saved": True})
