# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import os


def coalesce_blank(value):
    return value or ''

def BenchmarkTest09553(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = coalesce_blank(dotenv_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
