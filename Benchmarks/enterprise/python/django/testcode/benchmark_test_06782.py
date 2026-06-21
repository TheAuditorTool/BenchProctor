# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast
from app_runtime import db


def BenchmarkTest06782(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
