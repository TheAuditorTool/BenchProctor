# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest49259(request):
    upload_name = request.FILES['upload'].name
    data = default_blank(upload_name)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
