# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib
import ast


def BenchmarkTest06429(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    digest = str(data).encode().hex()
    return JsonResponse({'digest': str(digest)}, status=200)
