# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest65652(request, path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
