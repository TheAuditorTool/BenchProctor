# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import random
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest80270(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    random.seed(int(data) if str(data).isdigit() else 99)
    token = random.randint(0, 99)
    return JsonResponse({'token': str(token)}, status=200)
