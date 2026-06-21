# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import json


def BenchmarkTest50377(request):
    cookie_value = request.COOKIES.get('session_token', '')
    try:
        data = json.loads(cookie_value).get('value', cookie_value)
    except (json.JSONDecodeError, AttributeError):
        data = cookie_value
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
