# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


def BenchmarkTest09833(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
