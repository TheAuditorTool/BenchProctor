# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest63377(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    resp = JsonResponse({'status': 'ok'})
    resp.set_cookie('session', str(data))
    return resp
