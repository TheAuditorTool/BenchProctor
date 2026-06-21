# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest45116(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ' '.join(str(env_value).split())
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})
