# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest48527(request):
    env_value = os.environ.get('USER_INPUT', '')
    logging.info('User action: ' + str(env_value))
    return JsonResponse({"saved": True})
