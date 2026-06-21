# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


request_state: dict[str, str] = {}

def BenchmarkTest48726(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
