# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest68299(request):
    env_value = os.environ.get('USER_INPUT', '')
    if not str(env_value).isdigit():
        raise ValueError('invalid input: ' + str(env_value))
    return JsonResponse({"saved": True})
