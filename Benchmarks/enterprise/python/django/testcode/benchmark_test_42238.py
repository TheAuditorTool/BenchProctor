# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest42238(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    processed = data[:64]
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})
