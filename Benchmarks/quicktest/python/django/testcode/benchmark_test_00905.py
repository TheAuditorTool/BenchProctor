# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def BenchmarkTest00905(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
