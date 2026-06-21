# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import subprocess
import shlex


def BenchmarkTest11209(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    processed = shlex.quote(data)
    subprocess.run('echo ' + str(processed), shell=True)
    return JsonResponse({"saved": True})
