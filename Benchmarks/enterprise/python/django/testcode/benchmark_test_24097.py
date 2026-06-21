# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def BenchmarkTest24097(request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
