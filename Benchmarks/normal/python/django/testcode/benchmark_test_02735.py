# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest02735(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return JsonResponse({"saved": True})
