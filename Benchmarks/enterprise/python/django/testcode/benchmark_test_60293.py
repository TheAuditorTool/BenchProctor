# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast
from app_runtime import db


def BenchmarkTest60293(request):
    multipart_value = request.POST.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
