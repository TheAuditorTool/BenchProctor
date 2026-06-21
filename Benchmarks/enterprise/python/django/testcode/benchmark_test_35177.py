# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest35177(request):
    env_value = os.environ.get('USER_INPUT', '')
    os.system('echo ' + str(env_value))
    return JsonResponse({"saved": True})
