# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re
import os


def BenchmarkTest00235(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '{}'.format(env_value)
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
