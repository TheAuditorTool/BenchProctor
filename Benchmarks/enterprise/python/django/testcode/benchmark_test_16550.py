# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def BenchmarkTest16550(request):
    env_value = os.environ.get('USER_INPUT', '')
    subprocess.run('echo ' + str(env_value), shell=True)
    return JsonResponse({"saved": True})
