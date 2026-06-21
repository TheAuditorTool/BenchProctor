# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def ensure_str(value):
    return str(value)

def BenchmarkTest68847(request):
    raw_body = request.body.decode('utf-8')
    data = ensure_str(raw_body)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
