# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def BenchmarkTest16983(request):
    raw_body = request.body.decode('utf-8')
    data = str(raw_body).replace('\x00', '')
    subprocess.run([str(data), '--status'], shell=False)
    return JsonResponse({"saved": True})
