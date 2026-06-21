# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast
from app_runtime import db


def BenchmarkTest06300(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
