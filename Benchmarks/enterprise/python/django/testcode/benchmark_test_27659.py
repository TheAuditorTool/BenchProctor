# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import importlib


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest27659(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    importlib.import_module(str(processed))
    return JsonResponse({"saved": True})
