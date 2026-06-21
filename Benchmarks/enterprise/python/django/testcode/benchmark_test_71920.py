# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest71920(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    os.remove(str(data))
    return JsonResponse({"saved": True})
