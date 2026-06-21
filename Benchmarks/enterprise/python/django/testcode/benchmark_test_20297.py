# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import logging


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest20297(request):
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = handle(prop_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
