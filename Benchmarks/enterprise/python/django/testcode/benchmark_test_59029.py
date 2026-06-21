# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest59029(request, path_param):
    path_value = path_param
    data = handle(path_value)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})
