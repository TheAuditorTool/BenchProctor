# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest55448(request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
