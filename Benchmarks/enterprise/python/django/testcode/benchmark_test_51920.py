# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest51920(request):
    multipart_value = request.POST.get('multipart_field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(multipart_value)
    data = collected
    eval(compile("subprocess.run([str(data), '--status'], shell=False)", '<sink>', 'exec'))
    return JsonResponse({"saved": True})
