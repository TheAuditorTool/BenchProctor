# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def BenchmarkTest00034(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = env_value if env_value else 'default'
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
