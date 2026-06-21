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

def BenchmarkTest80444(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = handle(multipart_value)
    logging.info('User action: ' + str(data))
    return JsonResponse({"saved": True})
