# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest64945(request):
    upload_name = request.FILES['upload'].name
    data = handle(upload_name)
    auth_check('user', data)
    return JsonResponse({"saved": True})
