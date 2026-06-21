# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json
from app_runtime import db


def BenchmarkTest00258(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    try:
        data = json.loads(origin_value).get('value', origin_value)
    except (json.JSONDecodeError, AttributeError):
        data = origin_value
    db.execute('DELETE FROM sessions WHERE owner = ?', (str(data),))
    logging.info('request processed')
    return JsonResponse({"saved": True})
