# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest64294(request):
    xml_value = request.body.decode('utf-8')
    reader = make_reader(xml_value)
    data = reader()
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return JsonResponse({'error': 'forbidden'}, status=403)
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return JsonResponse({"saved": True})
