# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest34620(request):
    host_value = request.META.get('HTTP_HOST', '')
    reader = make_reader(host_value)
    data = reader()
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
