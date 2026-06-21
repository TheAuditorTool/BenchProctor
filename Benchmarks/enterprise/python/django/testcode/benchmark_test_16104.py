# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest16104(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
