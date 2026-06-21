# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest00161(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
