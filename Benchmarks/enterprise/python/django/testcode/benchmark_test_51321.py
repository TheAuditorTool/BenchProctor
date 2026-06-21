# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


def BenchmarkTest51321(request):
    env_value = os.environ.get('USER_INPUT', '')
    prefix = ''
    data = prefix + str(env_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
