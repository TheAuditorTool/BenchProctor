# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
from app_runtime import db


def BenchmarkTest51830(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
