# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest59469(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
