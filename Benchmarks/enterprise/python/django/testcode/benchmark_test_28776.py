# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import ast


def BenchmarkTest28776(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
