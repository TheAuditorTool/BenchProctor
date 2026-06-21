# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import re


request_state: dict[str, str] = {}

def BenchmarkTest28927(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return JsonResponse({"saved": True})
