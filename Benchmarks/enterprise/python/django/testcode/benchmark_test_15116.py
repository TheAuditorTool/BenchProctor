# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


request_state: dict[str, str] = {}

def BenchmarkTest15116(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
