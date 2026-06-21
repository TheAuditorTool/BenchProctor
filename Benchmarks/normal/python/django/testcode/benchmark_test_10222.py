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

def BenchmarkTest10222(request, path_param):
    path_value = path_param
    data = handle(path_value)
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return JsonResponse({"saved": True})
