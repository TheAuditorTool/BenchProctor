# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest47627(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
