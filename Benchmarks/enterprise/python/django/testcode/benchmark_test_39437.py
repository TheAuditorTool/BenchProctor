# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest39437(request, path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
