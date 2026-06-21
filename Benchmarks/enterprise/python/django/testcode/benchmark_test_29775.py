# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def ensure_str(value):
    return str(value)

def BenchmarkTest29775(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = ensure_str(env_value)
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
