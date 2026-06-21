# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest80150(request, path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
