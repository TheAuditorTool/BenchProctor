# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest52490(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
