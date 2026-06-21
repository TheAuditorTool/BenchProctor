# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import re


def BenchmarkTest01565(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return JsonResponse({'validated': str(data)}, status=200)
    return JsonResponse({"saved": True})
