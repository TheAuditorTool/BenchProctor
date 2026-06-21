# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest57915(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})
