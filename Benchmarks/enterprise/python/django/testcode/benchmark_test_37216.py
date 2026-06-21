# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest37216(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})
