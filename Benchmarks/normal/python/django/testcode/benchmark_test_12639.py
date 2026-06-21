# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12639(request):
    raw_body = request.body.decode('utf-8')
    ctx = RequestContext(raw_body)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
