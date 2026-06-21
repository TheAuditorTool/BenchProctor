# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest29174(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    eval(str(data))
    return JsonResponse({"saved": True})
