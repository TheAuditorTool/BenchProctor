# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest01699(request):
    env_value = os.environ.get('USER_INPUT', '')
    processed = shlex.quote(env_value)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
