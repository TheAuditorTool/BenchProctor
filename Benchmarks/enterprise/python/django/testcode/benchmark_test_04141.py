# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest04141(request, path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
