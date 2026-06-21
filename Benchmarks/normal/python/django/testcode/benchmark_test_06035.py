# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest06035(request):
    host_value = request.META.get('HTTP_HOST', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)
