# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import jwt


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest04871(request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = handle(secret_value)
    processed = data[:64]
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return JsonResponse({"saved": True})
