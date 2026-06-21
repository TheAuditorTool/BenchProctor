# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest79966(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    defusedxml.ElementTree.fromstring(str(data))
    return JsonResponse({"saved": True})
