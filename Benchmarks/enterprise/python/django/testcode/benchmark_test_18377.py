# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast


def BenchmarkTest18377(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    try:
        data = str(ast.literal_eval(prop_value))
    except (ValueError, SyntaxError):
        data = prop_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
