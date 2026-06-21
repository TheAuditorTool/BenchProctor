# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import shlex


def BenchmarkTest81048(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return JsonResponse({"saved": True})
