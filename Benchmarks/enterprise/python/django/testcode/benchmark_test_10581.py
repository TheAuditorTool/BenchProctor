# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest10581(request):
    env_value = os.environ.get('USER_INPUT', '')
    with open('output.csv', 'a') as fh:
        fh.write(str(env_value) + ',data\n')
    return JsonResponse({"saved": True})
