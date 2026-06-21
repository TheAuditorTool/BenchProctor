# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest45457(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
