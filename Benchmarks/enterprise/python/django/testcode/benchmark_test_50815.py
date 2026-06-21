# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import re
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest50815(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    if not re.fullmatch('^[\\w\\s./\\\\:<>=_\'\\"!()\\[\\]{}$-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    pickle.loads(processed.encode('latin-1'))
    return JsonResponse({"saved": True})
