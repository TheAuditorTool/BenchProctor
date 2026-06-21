# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast


def BenchmarkTest24525(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
