# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest38711(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    ctx = RequestContext(query_array)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
