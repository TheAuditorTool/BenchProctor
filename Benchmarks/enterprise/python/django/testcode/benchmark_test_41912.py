# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest41912(request, path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
