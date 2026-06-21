# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


request_state: dict[str, str] = {}

def BenchmarkTest30471(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return JsonResponse({'error': 'file error'}, status=500)
    return JsonResponse({"saved": True})
