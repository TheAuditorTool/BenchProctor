# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest16733(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
