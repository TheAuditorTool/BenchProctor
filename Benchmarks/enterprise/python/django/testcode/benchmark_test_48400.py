# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from app_runtime import auth_check


def BenchmarkTest48400(request):
    env_value = os.environ.get('USER_INPUT', '')
    auth_check('user', env_value)
    return JsonResponse({"saved": True})
