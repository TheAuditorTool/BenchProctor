# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest49001(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = default_blank(cookie_value)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
