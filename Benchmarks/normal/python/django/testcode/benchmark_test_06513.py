# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def ensure_str(value):
    return str(value)

def BenchmarkTest06513(request):
    upload_name = request.FILES['upload'].name
    data = ensure_str(upload_name)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
