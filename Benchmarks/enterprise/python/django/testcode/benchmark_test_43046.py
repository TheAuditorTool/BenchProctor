# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


request_state: dict[str, str] = {}

def BenchmarkTest43046(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    request_state['last_input'] = query_array
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
