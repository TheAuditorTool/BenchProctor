# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest48959(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = []
    for token in str(env_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
