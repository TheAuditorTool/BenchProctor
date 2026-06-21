# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest09365(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})
