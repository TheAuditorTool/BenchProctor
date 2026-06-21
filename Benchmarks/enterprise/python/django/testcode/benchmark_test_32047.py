# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest32047(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
