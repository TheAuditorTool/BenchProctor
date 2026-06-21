# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest74147(request):
    stdin_value = input('input: ')
    data = (lambda v: v.strip())(stdin_value)
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
