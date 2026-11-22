# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00055(request):
    raw_body = request.body.decode('utf-8')
    reader = make_reader(raw_body)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
