# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re


request_state: dict[str, str] = {}

def BenchmarkTest48831(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return JsonResponse({"saved": True})
