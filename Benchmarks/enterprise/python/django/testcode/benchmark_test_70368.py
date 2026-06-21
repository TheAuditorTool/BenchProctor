# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest70368(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
