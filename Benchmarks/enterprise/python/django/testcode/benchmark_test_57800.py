# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest57800(request, path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
