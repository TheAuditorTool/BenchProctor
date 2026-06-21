# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest42321(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % str(env_value)
    auth_check('user', data)
    return JsonResponse({"saved": True})
