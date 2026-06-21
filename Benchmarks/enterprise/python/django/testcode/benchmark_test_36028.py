# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest36028(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    return JsonResponse({'error': 'An internal error occurred'}, status=500)
