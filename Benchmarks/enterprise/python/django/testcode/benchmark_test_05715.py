# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import json


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest05715(request):
    json_value = json.loads(request.body.decode()).get('payload', '')
    reader = make_reader(json_value)
    data = reader()
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
