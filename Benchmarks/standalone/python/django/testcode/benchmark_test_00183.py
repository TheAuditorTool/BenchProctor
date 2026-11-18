# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import re


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest00183(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    if not re.fullmatch("^[a-zA-Z0-9 _.%\\-]+$", data):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    subprocess.Popen('echo ' + str(processed), shell=True).wait()
    return JsonResponse({"saved": True})
