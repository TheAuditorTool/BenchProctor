# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import tempfile


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63890(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return JsonResponse({"saved": True})
