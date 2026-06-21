# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


def BenchmarkTest51872(request):
    env_value = os.environ.get('USER_INPUT', '')
    def normalize(value):
        return value.strip()
    data = normalize(env_value)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
