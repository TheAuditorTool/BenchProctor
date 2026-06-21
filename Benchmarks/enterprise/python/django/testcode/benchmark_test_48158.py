# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import tempfile


request_state: dict[str, str] = {}

def BenchmarkTest48158(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return JsonResponse({"saved": True})
