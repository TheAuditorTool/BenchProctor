# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest15540(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"})
