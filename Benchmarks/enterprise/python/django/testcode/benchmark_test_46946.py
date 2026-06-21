# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import subprocess


def to_text(value):
    return str(value).strip()

def BenchmarkTest46946(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = to_text(ua_value)
    subprocess.run(['echo', data], shell=False)
    return JsonResponse({"saved": True})
