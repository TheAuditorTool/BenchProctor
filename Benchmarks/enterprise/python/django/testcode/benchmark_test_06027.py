# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest06027(request):
    cookie_value = request.COOKIES.get('session_token', '')
    reader = make_reader(cookie_value)
    data = reader()
    subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
