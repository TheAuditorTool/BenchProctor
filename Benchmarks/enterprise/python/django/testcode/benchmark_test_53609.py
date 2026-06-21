# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest53609(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
