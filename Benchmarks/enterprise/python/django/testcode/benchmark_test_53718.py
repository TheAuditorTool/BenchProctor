# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest53718(request, path_param):
    path_value = path_param
    data = str(path_value).replace('\x00', '')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
