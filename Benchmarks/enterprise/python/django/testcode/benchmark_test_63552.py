# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest63552(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
