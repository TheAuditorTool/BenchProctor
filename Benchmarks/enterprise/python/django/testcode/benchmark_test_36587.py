# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
from urllib.parse import unquote


def BenchmarkTest36587(request, path_param):
    path_value = path_param
    data = unquote(path_value)
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
