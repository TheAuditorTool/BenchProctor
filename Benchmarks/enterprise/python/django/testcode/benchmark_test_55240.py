# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import base64
from app_runtime import db


def BenchmarkTest55240(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
