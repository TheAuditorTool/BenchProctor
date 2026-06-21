# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest53647(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
