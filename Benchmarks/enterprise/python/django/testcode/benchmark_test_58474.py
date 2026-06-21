# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


def BenchmarkTest58474(request):
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
