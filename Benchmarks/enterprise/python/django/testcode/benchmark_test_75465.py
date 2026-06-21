# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
from app_runtime import db


def BenchmarkTest75465(request):
    env_value = os.environ.get('USER_INPUT', '')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(env_value),))
    logging.info('audit actor=%s action=revoke_sessions', str(env_value))
    return JsonResponse({"saved": True})
