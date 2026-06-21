# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os
import json
from app_runtime import db


def BenchmarkTest36343(request):
    env_value = os.environ.get('USER_INPUT', '')
    try:
        data = json.loads(env_value).get('value', env_value)
    except (json.JSONDecodeError, AttributeError):
        data = env_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
