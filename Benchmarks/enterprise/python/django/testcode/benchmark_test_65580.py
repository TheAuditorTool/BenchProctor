# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest65580(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
