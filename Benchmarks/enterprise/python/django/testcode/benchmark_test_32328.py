# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest32328(request):
    env_value = os.environ.get('USER_INPUT', '')
    subprocess.run([str(env_value), '--status'], shell=False)
    return JsonResponse({"saved": True})
