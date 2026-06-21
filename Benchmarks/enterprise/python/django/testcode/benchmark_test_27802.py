# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast


def BenchmarkTest27802(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    try:
        data = str(ast.literal_eval(query_array))
    except (ValueError, SyntaxError):
        data = query_array
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
