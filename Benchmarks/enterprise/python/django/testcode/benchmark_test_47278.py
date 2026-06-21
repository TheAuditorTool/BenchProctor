# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


def BenchmarkTest47278(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
