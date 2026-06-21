# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest55710(request):
    stdin_value = input('input: ')
    if stdin_value:
        data = stdin_value
    else:
        data = ''
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
