# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest44535(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
