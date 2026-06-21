# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest00695(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
