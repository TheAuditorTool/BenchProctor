# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import ast


def BenchmarkTest68895(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
