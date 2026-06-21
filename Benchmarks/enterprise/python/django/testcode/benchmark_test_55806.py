# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


request_state: dict[str, str] = {}

def BenchmarkTest55806(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
