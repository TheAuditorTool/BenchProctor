# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast
import re


def BenchmarkTest00151(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return JsonResponse({'validated': str(processed)}, status=200)
    return JsonResponse({"saved": True})
