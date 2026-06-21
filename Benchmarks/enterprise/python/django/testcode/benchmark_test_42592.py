# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest42592(request):
    with open('/etc/app/config.yaml', 'r') as fh:
        yaml_value = fh.read()
    ctx = RequestContext(yaml_value)
    data = ctx.payload
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
