# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
import ast


def BenchmarkTest24766(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    try:
        data = str(ast.literal_eval(json_value))
    except (ValueError, SyntaxError):
        data = json_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
