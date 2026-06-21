# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re


request_state: dict[str, str] = {}

def BenchmarkTest78941(request):
    user_id = request.GET.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    processed = re.sub(r'[A-Za-z0-9]{4,}', '****', str(data).replace('\r', '').replace('\n', ''))
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
