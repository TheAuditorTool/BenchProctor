# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json
from app_runtime import mq_client


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest40057(request):
    msg_value = mq_client.get_message().body
    ctx = RequestContext(msg_value)
    data = ctx.payload
    json.loads(data)
    return JsonResponse({"saved": True})
