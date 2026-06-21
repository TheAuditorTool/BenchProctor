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

def BenchmarkTest45013(request):
    query_array = request.GET.getlist('items')[0] if request.GET.getlist('items') else ''
    data = handle(query_array)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
