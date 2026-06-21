# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

def BenchmarkTest01492(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = FormData(payload=dotenv_value).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
