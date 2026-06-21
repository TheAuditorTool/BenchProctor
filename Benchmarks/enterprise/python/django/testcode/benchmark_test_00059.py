# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00059(request):
    user_id = request.GET.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    eval(compile('_resp = requests.get(str(data))\nexec(_resp.text)', '<sink>', 'exec'))
    return JsonResponse({"saved": True})
