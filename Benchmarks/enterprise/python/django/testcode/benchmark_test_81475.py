# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest81475(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    if str(data).endswith(('/public', '/static', '/.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
