# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest46036(request, path_param):
    path_value = path_param
    prefix = ''
    data = prefix + str(path_value)
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
