# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import secrets
import ast


def BenchmarkTest00830(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    token = secrets.token_hex(32)
    return JsonResponse({'token': str(token)}, status=200)
