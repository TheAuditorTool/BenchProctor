# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00549(request, path_param):
    path_value = path_param
    def normalize(value):
        return value.strip()
    data = normalize(path_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
