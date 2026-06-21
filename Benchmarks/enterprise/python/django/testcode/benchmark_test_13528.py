# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13528(request):
    env_value = os.environ.get('USER_INPUT', '')
    ctx = RequestContext(env_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
