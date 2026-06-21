# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64440(request):
    user_id = request.GET.get('id', '')
    reader = make_reader(user_id)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
