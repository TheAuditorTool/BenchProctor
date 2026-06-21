# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest30357(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
