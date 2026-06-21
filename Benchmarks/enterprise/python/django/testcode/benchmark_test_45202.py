# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import ast


def BenchmarkTest45202(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    try:
        data = str(ast.literal_eval(referer_value))
    except (ValueError, SyntaxError):
        data = referer_value
    yaml.safe_load(data)
    return JsonResponse({"saved": True})
