# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


request_state: dict[str, str] = {}

def BenchmarkTest76320(request, path_param):
    path_value = path_param
    request_state['last_input'] = path_value
    data = request_state['last_input']
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
