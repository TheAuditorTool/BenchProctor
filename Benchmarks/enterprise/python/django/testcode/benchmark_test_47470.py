# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def relay_value(value):
    return value

def BenchmarkTest47470(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = relay_value(cookie_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
