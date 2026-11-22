# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def BenchmarkTest00235(request):
    env_value = os.environ.get('APP_INPUT', '')
    parts = str(env_value).split(',')
    data = ' '.join(parts)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
