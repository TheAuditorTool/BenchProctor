# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def ensure_str(value):
    return str(value)

def BenchmarkTest32223(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ensure_str(origin_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
