# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast


def BenchmarkTest12018(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
