# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest00297(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
