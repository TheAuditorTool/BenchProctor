# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def BenchmarkTest41212(request):
    env_value = os.environ.get('USER_INPUT', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(env_value)
    data = collected
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
