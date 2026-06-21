# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import os


def ensure_str(value):
    return str(value)

def BenchmarkTest05547(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
