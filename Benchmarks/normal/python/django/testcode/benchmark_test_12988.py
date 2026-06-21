# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import ast


def BenchmarkTest12988(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    try:
        data = str(ast.literal_eval(ua_value))
    except (ValueError, SyntaxError):
        data = ua_value
    eval(compile("with open('/var/app/data/' + str(data), 'w') as fh:\n    fh.write('data')", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
