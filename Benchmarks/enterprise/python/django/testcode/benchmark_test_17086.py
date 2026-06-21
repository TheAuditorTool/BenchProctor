# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess


def relay_value(value):
    return value

def BenchmarkTest17086(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = relay_value(ua_value)
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
