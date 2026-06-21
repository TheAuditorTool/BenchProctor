# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex


def BenchmarkTest02026(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
