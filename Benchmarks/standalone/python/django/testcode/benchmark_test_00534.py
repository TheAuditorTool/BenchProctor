# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os
import re


def BenchmarkTest00534(request):
    env_value = os.environ.get('APP_INPUT', '')
    data = '%s' % str(env_value)
    if not re.fullmatch("^(asc|desc|name|created)$", str(data)):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
