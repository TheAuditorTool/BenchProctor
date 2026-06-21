# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest01076(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return JsonResponse({"saved": True})
