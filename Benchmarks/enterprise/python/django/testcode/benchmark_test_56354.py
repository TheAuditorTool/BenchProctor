# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest56354(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    globals()['counter'] = int(data)
    return JsonResponse({"saved": True})
