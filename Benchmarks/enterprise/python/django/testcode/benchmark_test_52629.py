# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import os


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest52629(request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
