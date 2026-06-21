# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest44841(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    subprocess.Popen('echo ' + str(data), shell=True).wait()
    return JsonResponse({"saved": True})
