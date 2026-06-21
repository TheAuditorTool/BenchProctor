# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import ast
from app_runtime import db


def BenchmarkTest05358(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
