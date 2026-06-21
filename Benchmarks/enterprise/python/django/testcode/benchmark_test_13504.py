# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13504(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
