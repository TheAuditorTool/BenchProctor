# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


request_state: dict[str, str] = {}

def BenchmarkTest38917(request):
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
