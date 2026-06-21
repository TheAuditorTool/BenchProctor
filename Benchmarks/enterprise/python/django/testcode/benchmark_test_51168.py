# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import base64


def BenchmarkTest51168(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = base64.b64decode(cookie_value).decode('utf-8', 'ignore')
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
