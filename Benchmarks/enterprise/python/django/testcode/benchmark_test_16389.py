# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import ast


def BenchmarkTest16389(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return JsonResponse({"saved": True})
