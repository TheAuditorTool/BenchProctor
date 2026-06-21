# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
import os


def relay_value(value):
    return value

def BenchmarkTest45718(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = relay_value(env_value)
    if not re.fullmatch('^[\\w\\s.;|&$`\'\\"_/\\-]+$', data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
