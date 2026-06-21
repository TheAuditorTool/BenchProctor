# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest13270(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    data = handle(json_value)
    checked_path = os.path.normpath(data)
    os.unlink('/var/app/data/' + str(checked_path))
    return JsonResponse({"saved": True})
