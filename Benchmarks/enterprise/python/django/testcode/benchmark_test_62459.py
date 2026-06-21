# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


def BenchmarkTest62459(request):
    env_value = os.environ.get('USER_INPUT', '')
    importlib.import_module(str(env_value))
    return JsonResponse({"saved": True})
