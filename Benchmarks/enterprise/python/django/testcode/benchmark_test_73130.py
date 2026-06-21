# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex
import os


def BenchmarkTest73130(request):
    env_value = os.environ.get('USER_INPUT', '')
    processed = shlex.quote(env_value)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
