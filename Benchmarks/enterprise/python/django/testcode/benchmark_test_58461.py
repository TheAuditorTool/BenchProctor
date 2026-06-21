# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def BenchmarkTest58461(request):
    stdin_value = input('input: ')
    data = ' '.join(str(stdin_value).split())
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
