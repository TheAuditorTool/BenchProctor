# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest00401(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
