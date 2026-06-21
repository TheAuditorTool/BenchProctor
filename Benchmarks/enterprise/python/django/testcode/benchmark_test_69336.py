# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import ast


def BenchmarkTest69336(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = str(ast.literal_eval(prop_value))
    except (ValueError, SyntaxError):
        data = prop_value
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
