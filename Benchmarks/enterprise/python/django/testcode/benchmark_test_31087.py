# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def coalesce_blank(value):
    return value or ''

def BenchmarkTest31087(request):
    stdin_value = input('input: ')
    data = coalesce_blank(stdin_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
