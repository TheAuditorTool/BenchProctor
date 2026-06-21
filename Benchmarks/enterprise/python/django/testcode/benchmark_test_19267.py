# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest19267(request):
    host_value = request.META.get('HTTP_HOST', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    processed = data[:64]
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(processed))
    return redirect(target)
