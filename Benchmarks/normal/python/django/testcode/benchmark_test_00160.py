# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest00160(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = bytes.fromhex(cookie_value).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
