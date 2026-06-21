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

def BenchmarkTest67956(request):
    user_id = request.GET.get('id', '')
    data = handle(user_id)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
