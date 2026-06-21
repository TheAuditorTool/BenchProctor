# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def to_text(value):
    return str(value).strip()

def BenchmarkTest08852(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = to_text(env_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
