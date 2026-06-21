# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest34439(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    with open('output.csv', 'a') as fh:
        fh.write(str(data) + ',data\n')
    return JsonResponse({"saved": True})
