# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def BenchmarkTest19286(request):
    env_value = os.environ.get('USER_INPUT', '')
    parts = str(env_value).split(',')
    data = ','.join(parts)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
