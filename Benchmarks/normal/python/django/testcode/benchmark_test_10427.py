# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest10427(request):
    stdin_value = input('input: ')
    data = default_blank(stdin_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
