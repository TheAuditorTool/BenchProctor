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

def BenchmarkTest41450(request):
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = handle(dotenv_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
