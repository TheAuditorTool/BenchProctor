# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
from app_runtime import db


def BenchmarkTest59444(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('audit actor=%s action=revoke_sessions', str(data))
    return JsonResponse({"saved": True})
