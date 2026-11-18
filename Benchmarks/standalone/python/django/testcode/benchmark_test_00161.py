# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00161(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '{}'.format(env_value)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
