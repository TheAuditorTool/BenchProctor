# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


request_state: dict[str, str] = {}

def BenchmarkTest80757(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    request_state['last_input'] = header_value
    data = request_state['last_input']
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
