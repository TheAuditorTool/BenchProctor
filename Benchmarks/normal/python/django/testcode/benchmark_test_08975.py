# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest08975(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
