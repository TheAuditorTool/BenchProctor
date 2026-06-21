# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest75343(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
