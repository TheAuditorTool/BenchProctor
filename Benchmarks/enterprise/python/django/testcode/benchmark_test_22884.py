# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
from app_runtime import db


def BenchmarkTest22884(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
