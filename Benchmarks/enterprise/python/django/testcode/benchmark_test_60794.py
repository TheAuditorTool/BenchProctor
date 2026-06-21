# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest60794(request, path_param):
    path_value = path_param
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(path_value)
    data = collected
    eval(compile("subprocess.Popen('echo ' + str(data), shell=True).wait()", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
