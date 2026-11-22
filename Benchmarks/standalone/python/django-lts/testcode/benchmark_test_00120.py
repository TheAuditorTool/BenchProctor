# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def BenchmarkTest00120(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
