# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import re
import os


def BenchmarkTest01485(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = data
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
