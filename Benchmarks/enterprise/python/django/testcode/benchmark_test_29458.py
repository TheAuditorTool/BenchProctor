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

def BenchmarkTest29458(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = handle(auth_header)
    processed = data[:64]
    logging.info('User action: ' + str(processed))
    return JsonResponse({"saved": True})
