# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest04157(request):
    raw_body = request.body.decode('utf-8')
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
