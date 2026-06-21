# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest02559(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
