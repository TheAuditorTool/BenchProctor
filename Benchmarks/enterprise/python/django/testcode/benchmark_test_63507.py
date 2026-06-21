# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def BenchmarkTest63507(request):
    cookie_value = request.COOKIES.get('session_token', '')
    data = f'{cookie_value}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
