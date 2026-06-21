# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest41647(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
