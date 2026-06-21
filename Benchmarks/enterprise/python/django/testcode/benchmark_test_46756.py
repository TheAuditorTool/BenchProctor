# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
import os


def BenchmarkTest46756(request):
    env_value = os.environ.get('USER_INPUT', '')
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(env_value)):
        return JsonResponse({'error': 'invalid input'}, status=400)
    processed = env_value
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
