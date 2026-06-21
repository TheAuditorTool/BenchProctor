# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


def BenchmarkTest00498(request):
    cookie_value = request.COOKIES.get('session_token', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(cookie_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(cookie_value))
    return JsonResponse({"saved": True})
