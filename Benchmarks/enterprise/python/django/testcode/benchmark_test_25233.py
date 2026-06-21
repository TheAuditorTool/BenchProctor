# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest25233(request):
    stdin_value = input('input: ')
    data, _sep, _rest = str(stdin_value).partition('\x00')
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
