# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import ast


def BenchmarkTest23900(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    try:
        data = str(ast.literal_eval(forwarded_ip))
    except (ValueError, SyntaxError):
        data = forwarded_ip
    if not re.match(r'^.{1,256}$', str(data)):
        return JsonResponse({'error': 'schema invalid'}, status=400)
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JsonResponse({'authenticated': True}, status=200)
    return JsonResponse({"saved": True})
