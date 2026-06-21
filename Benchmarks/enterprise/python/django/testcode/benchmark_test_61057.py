# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import time


def BenchmarkTest61057(request):
    xml_value = request.body.decode('utf-8')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(xml_value)
    data = collected
    if time.time() > 1000000000:
        subprocess.run('echo ' + str(data), shell=True)
    return JsonResponse({"saved": True})
