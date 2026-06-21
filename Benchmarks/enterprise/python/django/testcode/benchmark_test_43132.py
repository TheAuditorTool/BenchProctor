# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


def relay_value(value):
    return value

def BenchmarkTest43132(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
