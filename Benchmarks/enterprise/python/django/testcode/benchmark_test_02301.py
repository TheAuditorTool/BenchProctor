# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest02301(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '{}'.format(env_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
