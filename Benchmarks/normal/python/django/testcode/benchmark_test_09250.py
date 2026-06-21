# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09250(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return JsonResponse({"saved": True})
