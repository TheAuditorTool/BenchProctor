# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest66141(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
