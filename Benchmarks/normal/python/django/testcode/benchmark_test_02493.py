# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import ast
import socket


def BenchmarkTest02493(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    try:
        data = str(ast.literal_eval(auth_header))
    except (ValueError, SyntaxError):
        data = auth_header
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    s = socket.create_connection((str(data), 80))
    s.close()
    return JsonResponse({"saved": True})
