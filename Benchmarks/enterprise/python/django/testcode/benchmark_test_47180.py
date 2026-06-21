# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


request_state: dict[str, str] = {}

def BenchmarkTest47180(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    request_state['last_input'] = dotenv_value
    data = request_state['last_input']
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
